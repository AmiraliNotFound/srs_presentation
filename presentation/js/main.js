/**
 * ============================================================================
 * SHOCK RESPONSE SPECTRUM (SRS) — PRESENTATION CONTROLLER ENGINE
 * Department of Mechanical Engineering — University of Tehran
 * ============================================================================
 * Features:
 *  - Slide & Fragment State Machine (Bidirectional)
 *  - KaTeX Mathematical Auto-Rendering with local/CDN resilience
 *  - High-Efficiency Video Preload & Smooth Playback Manager
 *  - Real-Time Slide & Speaker Pacing Countdown Timer
 *  - Phase 4 Mobile Companion Hook & WebSocket Event Telemetry
 *  - Presenter Laser Pointer & Fullscreen Utilities
 */

class PresentationController {
  constructor() {
    // DOM Elements
    this.slides = Array.from(document.querySelectorAll('.slide'));
    this.totalSlides = this.slides.length;
    this.currentSlideIndex = 0;
    this.currentFragmentIndex = -1;

    // HUD Elements
    this.speakerBadge = document.getElementById('speaker-badge');
    this.speakerNameDisplay = document.getElementById('speaker-name-display');
    this.slideTimerDisplay = document.getElementById('slide-timer');
    this.pacingIndicator = document.getElementById('timer-pacing-indicator');
    this.currentSlideNumDisplay = document.getElementById('current-slide-num');
    this.totalSlideNumDisplay = document.getElementById('total-slide-num');
    this.progressBar = document.getElementById('progress-bar');
    this.progressSegments = document.getElementById('progress-segments');
    this.footerSpeakerBadge = document.getElementById('footer-speaker-badge');
    this.footerElapsedTime = document.getElementById('footer-elapsed-time');

    // Controls & Modals
    this.btnPrev = document.getElementById('btn-prev');
    this.btnNext = document.getElementById('btn-next');
    this.btnFullscreen = document.getElementById('btn-fullscreen');
    this.btnShortcuts = document.getElementById('btn-shortcuts');
    this.shortcutsModal = document.getElementById('shortcuts-modal');
    this.btnCloseModal = document.getElementById('btn-close-modal');
    this.laserCanvas = document.getElementById('laser-canvas');

    // Timer & Telemetry State
    this.slideSecondsRemaining = 90;
    this.slideTimeBudget = 90;
    this.timerInterval = null;
    this.isTimerPaused = false;
    this.presentationElapsedSeconds = 0;
    this.presentationInterval = null;

    // Video Cache
    this.videoPreloadCache = new Map();
    this.laserActive = false;

    // Initialize Engine
    this.init();
  }

  /**
   * Initializes all subsystems.
   */
  init() {
    console.log(`[SRS Engine] Initializing ${this.totalSlides} slides...`);
    this.totalSlideNumDisplay.textContent = String(this.totalSlides).padStart(2, '0');

    this.buildProgressTicks();
    this.bindEvents();
    this.initLaserPointer();
    this.initKaTeX();
    this.startPresentationClock();

    // Initial slide activation
    this.goToSlide(0, false);
  }

  /**
   * Generates progress bar segment markers with speaker boundaries.
   */
  buildProgressTicks() {
    this.progressSegments.innerHTML = '';
    for (let i = 0; i < this.totalSlides; i++) {
      const tick = document.createElement('div');
      tick.classList.add('progress-segment-tick');
      // Speaker division boundaries: Slide 6->7 (Speaker 1->2) and Slide 13->14 (Speaker 2->3)
      if (i === 6 || i === 13) {
        tick.classList.add('speaker-split');
      }
      this.progressSegments.appendChild(tick);
    }
  }

  /**
   * Safe KaTeX auto-rendering on the presentation deck.
   */
  initKaTeX() {
    const renderMath = () => {
      if (window.renderMathInElement) {
        try {
          window.renderMathInElement(document.body, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false },
              { left: '\\[', right: '\\]', display: true },
              { left: '\\(', right: '\\)', display: false }
            ],
            throwOnError: false
          });
          console.log('[SRS Engine] KaTeX formulas rendered successfully.');
        } catch (err) {
          console.warn('[SRS Engine] KaTeX auto-render encountered an error:', err);
        }
      } else {
        // Retry if script still loading asynchronously
        setTimeout(renderMath, 300);
      }
    };
    renderMath();
  }

  /**
   * Event listeners binding.
   */
  bindEvents() {
    // Keyboard navigation
    window.addEventListener('keydown', (e) => this.handleKeyDown(e));

    // Button controls
    this.btnNext.addEventListener('click', () => this.next());
    this.btnPrev.addEventListener('click', () => this.prev());
    this.btnFullscreen.addEventListener('click', () => this.toggleFullscreen());
    this.btnShortcuts.addEventListener('click', () => this.toggleShortcutsModal());
    this.btnCloseModal.addEventListener('click', () => this.toggleShortcutsModal(false));

    // Click outside modal to close
    this.shortcutsModal.addEventListener('click', (e) => {
      if (e.target === this.shortcutsModal) this.toggleShortcutsModal(false);
    });

    // Window resize handler for scaling
    window.addEventListener('resize', () => {
      if (this.laserActive) this.resizeLaserCanvas();
    });
  }

  /**
   * Handles keyboard navigation events.
   */
  handleKeyDown(e) {
    // Ignore input if user is in an input field
    if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

    switch (e.code) {
      case 'ArrowRight':
      case 'Space':
      case 'PageDown':
        e.preventDefault();
        this.next();
        break;

      case 'ArrowLeft':
      case 'PageUp':
        e.preventDefault();
        this.prev();
        break;

      case 'Home':
        e.preventDefault();
        this.goToSlide(0);
        break;

      case 'End':
        e.preventDefault();
        this.goToSlide(this.totalSlides - 1);
        break;

      case 'KeyF':
        e.preventDefault();
        this.toggleFullscreen();
        break;

      case 'KeyL':
        e.preventDefault();
        this.toggleLaser();
        break;

      case 'KeyT':
        e.preventDefault();
        this.toggleTimerPause();
        break;

      case 'KeyH':
      case 'Slash':
        if (e.key === '?' || e.code === 'KeyH') {
          e.preventDefault();
          this.toggleShortcutsModal();
        }
        break;

      case 'Escape':
        if (!this.shortcutsModal.classList.contains('hidden')) {
          this.toggleShortcutsModal(false);
        }
        break;
    }
  }

  /**
   * Advances forward: either reveals next fragment, or advances to next slide.
   */
  next() {
    const currentSlide = this.slides[this.currentSlideIndex];
    const fragments = Array.from(currentSlide.querySelectorAll('.fragment'));

    // Check if there are unrevealed fragments
    if (this.currentFragmentIndex < fragments.length - 1) {
      this.currentFragmentIndex++;
      this.revealFragment(fragments, this.currentFragmentIndex);
    } else {
      // Advance to next slide if available
      if (this.currentSlideIndex < this.totalSlides - 1) {
        this.goToSlide(this.currentSlideIndex + 1);
      }
    }
  }

  /**
   * Reverses backward: either hides previous fragment, or jumps to previous slide.
   */
  prev() {
    const currentSlide = this.slides[this.currentSlideIndex];
    const fragments = Array.from(currentSlide.querySelectorAll('.fragment'));

    if (this.currentFragmentIndex >= 0) {
      this.hideFragment(fragments, this.currentFragmentIndex);
      this.currentFragmentIndex--;
    } else {
      // Move to previous slide and reveal all its fragments
      if (this.currentSlideIndex > 0) {
        this.goToSlide(this.currentSlideIndex - 1, true);
      }
    }
  }

  /**
   * Reveals a specific fragment.
   */
  revealFragment(fragments, index) {
    if (fragments[index]) {
      fragments[index].classList.add('visible');
    }
  }

  /**
   * Hides a specific fragment.
   */
  hideFragment(fragments, index) {
    if (fragments[index]) {
      fragments[index].classList.remove('visible');
    }
  }

  /**
   * Transitions to target slide index.
   * @param {number} targetIndex - Target slide index (0 to totalSlides - 1).
   * @param {boolean} showAllFragments - If true, reveals all fragments (for back navigation).
   */
  goToSlide(targetIndex, showAllFragments = false) {
    if (targetIndex < 0 || targetIndex >= this.totalSlides) return;

    // Pause outgoing slide video
    const currentSlide = this.slides[this.currentSlideIndex];
    if (currentSlide) {
      currentSlide.classList.remove('active');
      this.handleVideoExit(currentSlide);
    }

    // Set new slide active
    this.currentSlideIndex = targetIndex;
    const newSlide = this.slides[targetIndex];
    newSlide.classList.add('active');

    // Manage fragments
    const fragments = Array.from(newSlide.querySelectorAll('.fragment'));
    if (showAllFragments) {
      fragments.forEach(f => f.classList.add('visible'));
      this.currentFragmentIndex = fragments.length - 1;
    } else {
      fragments.forEach(f => f.classList.remove('visible'));
      this.currentFragmentIndex = -1;
    }

    // Update telemetry, timers, and HUD
    this.updateHUD(newSlide);
    this.resetSlideTimer(newSlide);
    this.handleVideoEnter(newSlide);
    this.preloadNextVideo(targetIndex + 1);

    // Dispatch Phase 4 Companion Hook
    this.dispatchSlideChangeEvent(newSlide, fragments.length);
  }

  /**
   * Updates all HUD telemetry badges and progress indicators.
   */
  updateHUD(slide) {
    const slideNum = parseInt(slide.dataset.slideNum, 10);
    const speaker = slide.dataset.speaker || 'person1';
    const speakerName = slide.dataset.speakerName || 'Speaker';

    // Slide Counter
    this.currentSlideNumDisplay.textContent = String(slideNum).padStart(2, '0');

    // Progress Bar Fill
    const progressPercent = ((this.currentSlideIndex + 1) / this.totalSlides) * 100;
    this.progressBar.style.width = `${progressPercent}%`;

    // Speaker Pill Badge
    this.speakerBadge.className = 'speaker-pill';
    if (speaker === 'person1') {
      this.speakerBadge.classList.add('speaker-p1');
      this.footerSpeakerBadge.textContent = 'P1: 00:00 - 15:00';
    } else if (speaker === 'person2') {
      this.speakerBadge.classList.add('speaker-p2');
      this.footerSpeakerBadge.textContent = 'P2: 15:00 - 30:00';
    } else {
      this.speakerBadge.classList.add('speaker-p3');
      this.footerSpeakerBadge.textContent = 'P3: 30:00 - 45:00';
    }
    this.speakerNameDisplay.textContent = speakerName;
  }

  /**
   * Resets and restarts the countdown timer for the active slide.
   */
  resetSlideTimer(slide) {
    if (this.timerInterval) clearInterval(this.timerInterval);

    this.slideTimeBudget = parseInt(slide.dataset.timeBudget, 10) || 120;
    this.slideSecondsRemaining = this.slideTimeBudget;
    this.isTimerPaused = false;
    this.updateTimerDisplay();

    this.timerInterval = setInterval(() => {
      if (!this.isTimerPaused) {
        this.slideSecondsRemaining--;
        this.updateTimerDisplay();
      }
    }, 1000);
  }

  /**
   * Formats and renders countdown time in MM:SS.
   */
  updateTimerDisplay() {
    const isOvertime = this.slideSecondsRemaining < 0;
    const absSeconds = Math.abs(this.slideSecondsRemaining);
    const mins = Math.floor(absSeconds / 60);
    const secs = absSeconds % 60;
    const formatted = `${isOvertime ? '-' : ''}${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

    this.slideTimerDisplay.textContent = formatted;

    // Visual pacing indicator (Green = On Pace, Red = Overtime)
    if (isOvertime) {
      this.pacingIndicator.className = 'pacing-dot overtime';
      this.slideTimerDisplay.style.color = 'var(--accent-danger)';
    } else {
      this.pacingIndicator.className = 'pacing-dot on-pace';
      this.slideTimerDisplay.style.color = 'var(--text-primary)';
    }
  }

  /**
   * Master 45-minute cumulative lecture clock.
   */
  startPresentationClock() {
    if (this.presentationInterval) clearInterval(this.presentationInterval);

    this.presentationInterval = setInterval(() => {
      this.presentationElapsedSeconds++;
      const mins = Math.floor(this.presentationElapsedSeconds / 60);
      const secs = this.presentationElapsedSeconds % 60;
      this.footerElapsedTime.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')} / 45:00`;
    }, 1000);
  }

  /**
   * Video Playback Manager: smooth playback on slide entry.
   */
  handleVideoEnter(slide) {
    const video = slide.querySelector('video.manim-video');
    if (!video) return;

    const videoSrc = video.dataset.src;
    if (videoSrc && (!video.src || video.src === '')) {
      video.src = videoSrc;
    }

    video.currentTime = 0;
    const playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise
        .then(() => {
          video.classList.add('loaded-video');
        })
        .catch((err) => {
          // Graceful fallback: If MP4 is not yet rendered, keep wireframe placeholder visible
          console.info(`[SRS Engine] Note: Video for scene '${slide.dataset.manimScene}' not yet rendered or autoplay blocked. Wireframe fallback active.`, err.message);
          video.classList.remove('loaded-video');
        });
    }
  }

  /**
   * Video Pause on slide exit.
   */
  handleVideoExit(slide) {
    const video = slide.querySelector('video.manim-video');
    if (video) {
      video.pause();
    }
  }

  /**
   * Asynchronous Preload Manager: buffers next slide's video to avoid stall.
   */
  preloadNextVideo(nextIndex) {
    if (nextIndex >= this.totalSlides) return;
    const nextSlide = this.slides[nextIndex];
    const nextVideo = nextSlide.querySelector('video.manim-video');
    if (!nextVideo || !nextVideo.dataset.src) return;

    const src = nextVideo.dataset.src;
    if (!this.videoPreloadCache.has(src)) {
      const preloadLink = document.createElement('link');
      preloadLink.rel = 'preload';
      preloadLink.as = 'video';
      preloadLink.href = src;
      document.head.appendChild(preloadLink);
      this.videoPreloadCache.set(src, true);
      console.log(`[SRS Engine] Preloading video for slide ${nextIndex + 1}: ${src}`);
    }
  }

  /**
   * Dispatches custom event for Phase 4 WebSocket Companion.
   */
  dispatchSlideChangeEvent(slide, totalFragments) {
    const payload = {
      slideId: slide.dataset.slideId,
      slideNum: parseInt(slide.dataset.slideNum, 10),
      speaker: slide.dataset.speaker,
      speakerName: slide.dataset.speakerName,
      timeBudget: parseInt(slide.dataset.timeBudget, 10),
      quizTrigger: slide.dataset.quizTrigger || null,
      mobileSummary: slide.dataset.mobileSummary || '',
      manimScene: slide.dataset.manimScene || '',
      fragmentIndex: this.currentFragmentIndex,
      totalFragments: totalFragments,
      timestamp: new Date().toISOString()
    };

    // Custom window event
    const event = new CustomEvent('slidechange', { detail: payload });
    window.dispatchEvent(event);

    console.log(`[SRS Engine &bull; Slide Event] -> Slide ${payload.slideNum} (${payload.slideId}) | Speaker: ${payload.speaker} | Quiz: ${payload.quizTrigger || 'None'}`);

    // If Phase 4 WebSocket client is active, transmit immediately
    if (window.SRS_SOCKET && window.SRS_SOCKET.readyState === WebSocket.OPEN) {
      window.SRS_SOCKET.send(JSON.stringify({ type: 'SLIDE_CHANGE', data: payload }));
    }
  }

  /**
   * Toggles fullscreen presentation mode.
   */
  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {
        console.warn(`Error attempting to enable fullscreen: ${err.message}`);
      });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  /**
   * Toggles presenter laser pointer overlay.
   */
  toggleLaser() {
    this.laserActive = !this.laserActive;
    if (this.laserActive) {
      this.laserCanvas.classList.remove('hidden');
      this.resizeLaserCanvas();
      console.log('[SRS Engine] Laser Pointer: ACTIVE (Press L to disable)');
    } else {
      this.laserCanvas.classList.add('hidden');
      console.log('[SRS Engine] Laser Pointer: OFF');
    }
  }

  /**
   * Laser pointer mouse tracking setup.
   */
  initLaserPointer() {
    const ctx = this.laserCanvas.getContext('2d');
    this.resizeLaserCanvas();

    window.addEventListener('mousemove', (e) => {
      if (!this.laserActive) return;
      ctx.clearRect(0, 0, this.laserCanvas.width, this.laserCanvas.height);

      // Red laser dot with outer glowing aura
      const x = e.clientX;
      const y = e.clientY;

      // Glow
      const gradient = ctx.createRadialGradient(x, y, 2, x, y, 16);
      gradient.addColorStop(0, 'rgba(230, 57, 70, 0.9)');
      gradient.addColorStop(0.5, 'rgba(230, 57, 70, 0.4)');
      gradient.addColorStop(1, 'rgba(230, 57, 70, 0)');

      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(x, y, 16, 0, Math.PI * 2);
      ctx.fill();

      // Core bright center
      ctx.fillStyle = '#fff';
      ctx.beginPath();
      ctx.arc(x, y, 3, 0, Math.PI * 2);
      ctx.fill();
    });
  }

  resizeLaserCanvas() {
    this.laserCanvas.width = window.innerWidth;
    this.laserCanvas.height = window.innerHeight;
  }

  /**
   * Toggles pause on slide countdown timer.
   */
  toggleTimerPause() {
    this.isTimerPaused = !this.isTimerPaused;
    console.log(`[SRS Engine] Timer ${this.isTimerPaused ? 'PAUSED' : 'RESUMED'}`);
  }

  /**
   * Toggles shortcuts help modal.
   */
  toggleShortcutsModal(forceState) {
    if (forceState !== undefined) {
      if (forceState) this.shortcutsModal.classList.remove('hidden');
      else this.shortcutsModal.classList.add('hidden');
    } else {
      this.shortcutsModal.classList.toggle('hidden');
    }
  }
}

// Global initialization on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.srsPresentation = new PresentationController();
});
