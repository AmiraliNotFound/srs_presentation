/**
 * ============================================================================
 * SHOCK RESPONSE SPECTRUM (SRS) — 3BLUE1BROWN FULLSCREEN CONTROLLER ENGINE
 * Department of Mechanical Engineering — University of Tehran
 * ============================================================================
 * Features:
 *  - Zero Website Chrome: 100% full-bleed 16:9 Manim canvas
 *  - Slide State Machine & Fragment Stepper (Bidirectional)
 *  - Hidden Rehearsal Presenter HUD (Toggled via 'H' key)
 *  - Mouse Cursor Auto-Hide (2s inactivity timeout)
 *  - Pure Keyboard Navigation (Arrows, Space, Home/End, F, H) & Mouse Click
 *  - Smooth Manim Video Preload & Graceful Watermark Fallback
 *  - Phase 4 Mobile Companion Hook & WebSocket Event Telemetry
 *  - Mathematical KaTeX Auto-Rendering
 */

class PresentationController {
  constructor() {
    // Stage & Slide DOM Elements
    this.stage = document.getElementById('stage');
    this.slides = Array.from(document.querySelectorAll('.slide'));
    this.totalSlides = this.slides.length;
    this.currentSlideIndex = 0;
    this.currentFragmentIndex = -1;

    // Rehearsal Presenter HUD Elements
    this.hud = document.getElementById('presenter-hud');
    this.hudSlideNum = document.getElementById('hud-slide-num');
    this.hudTotalSlides = document.getElementById('hud-total-slides');
    this.hudSpeaker = document.getElementById('hud-speaker');
    this.hudElapsed = document.getElementById('hud-elapsed');
    this.hudSlideTimer = document.getElementById('hud-slide-timer');
    this.hudBudget = document.getElementById('hud-budget');
    this.hudScene = document.getElementById('hud-scene');

    // Timer & Telemetry State
    this.slideSecondsRemaining = 90;
    this.slideTimeBudget = 90;
    this.timerInterval = null;
    this.isTimerPaused = false;
    this.presentationElapsedSeconds = 0;
    this.presentationInterval = null;

    // Cursor Inactivity Timer
    this.cursorTimer = null;

    // Video Cache
    this.videoPreloadCache = new Map();

    // Initialize Engine
    this.init();
  }

  /**
   * Initializes all stage subsystems.
   */
  init() {
    console.log(`[SRS Engine] 3Blue1Brown Fullscreen Stage initialized: ${this.totalSlides} slides loaded.`);
    if (this.hudTotalSlides) {
      this.hudTotalSlides.textContent = String(this.totalSlides).padStart(2, '0');
    }

    this.initVideos();
    this.bindEvents();
    this.initCursorHiding();
    this.initKaTeX();
    this.startPresentationClock();

    // Activate initial slide
    this.goToSlide(0, false);
  }

  /**
   * Set up video event listeners across all slides.
   */
  initVideos() {
    this.slides.forEach((slide) => {
      const video = slide.querySelector('video.stage-video');
      if (video) {
        video.addEventListener('canplay', () => video.classList.add('loaded'));
        video.addEventListener('playing', () => video.classList.add('playing'));
        video.addEventListener('error', () => video.classList.remove('playing', 'loaded'));
      }
    });
  }

  /**
   * Bind keyboard, mouse, and presentation controls.
   */
  bindEvents() {
    // Keyboard navigation
    window.addEventListener('keydown', (e) => this.handleKeyDown(e));

    // Mouse click to advance
    document.addEventListener('click', (e) => {
      if (e.target.closest('button, a, input, textarea, select')) return;
      this.next();
    });
  }

  /**
   * Auto-hide mouse cursor after 2 seconds of inactivity.
   */
  initCursorHiding() {
    const showCursor = () => {
      document.body.classList.remove('cursor-hidden');
      clearTimeout(this.cursorTimer);
      this.cursorTimer = setTimeout(() => {
        document.body.classList.add('cursor-hidden');
      }, 2000);
    };

    window.addEventListener('mousemove', showCursor);
    window.addEventListener('mousedown', showCursor);
    window.addEventListener('keydown', showCursor);
    showCursor();
  }

  /**
   * Safe KaTeX auto-rendering for any TeX expressions.
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
          console.log('[SRS Engine] KaTeX formulas rendered.');
        } catch (err) {
          console.warn('[SRS Engine] KaTeX render error:', err);
        }
      } else {
        setTimeout(renderMath, 300);
      }
    };
    renderMath();
  }

  /**
   * Handles keyboard navigation events.
   */
  handleKeyDown(e) {
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

      case 'KeyH':
        e.preventDefault();
        this.togglePresenterHud();
        break;
    }
  }

  /**
   * Toggles the secret rehearsal presenter HUD.
   */
  togglePresenterHud() {
    if (!this.hud) return;
    const isVisible = this.hud.classList.toggle('visible');
    this.hud.style.display = isVisible ? 'block' : 'none';
    this.hud.setAttribute('aria-hidden', isVisible ? 'false' : 'true');
    console.log(`[SRS Engine] Rehearsal HUD: ${isVisible ? 'VISIBLE' : 'HIDDEN'}`);
  }

  /**
   * Advances forward: either reveals next fragment, or advances to next slide.
   */
  next() {
    const currentSlide = this.slides[this.currentSlideIndex];
    const fragments = Array.from(currentSlide.querySelectorAll('.fragment'));

    if (this.currentFragmentIndex < fragments.length - 1) {
      this.currentFragmentIndex++;
      this.revealFragment(fragments, this.currentFragmentIndex);
    } else {
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
      if (this.currentSlideIndex > 0) {
        this.goToSlide(this.currentSlideIndex - 1, true);
      }
    }
  }

  /**
   * Reveals a specific fragment.
   */
  revealFragment(fragments, index) {
    const fragment = fragments[index];
    if (fragment) {
      fragment.classList.add('visible');
      const slide = this.slides[this.currentSlideIndex];
      const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
      if (video && fragment.dataset.videoAction === 'resume') {
        video.play();
      }
    }
  }

  /**
   * Hides a specific fragment.
   */
  hideFragment(fragments, index) {
    const fragment = fragments[index];
    if (fragment) {
      fragment.classList.remove('visible');
      const slide = this.slides[this.currentSlideIndex];
      const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
      if (video && fragment.dataset.videoAction === 'resume') {
        video.currentTime = 0;
        video.pause();
      }
    }
  }

  /**
   * Transitions to target slide index.
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
   * Updates hidden presenter rehearsal HUD metrics.
   */
  updateHUD(slide) {
    if (!this.hud) return;

    const slideNum = parseInt(slide.dataset.slideNum, 10);
    const speaker = slide.dataset.speaker || 'person1';
    const speakerName = slide.dataset.speakerName || 'Speaker';
    const budget = parseInt(slide.dataset.timeBudget, 10) || 90;
    const scene = slide.dataset.manimScene || 'Scene';

    if (this.hudSlideNum) this.hudSlideNum.textContent = String(slideNum).padStart(2, '0');
    if (this.hudTotalSlides) this.hudTotalSlides.textContent = String(this.totalSlides).padStart(2, '0');
    if (this.hudSpeaker) {
      this.hudSpeaker.textContent = speakerName;
      this.hudSpeaker.className = `hud-val ${speaker.toLowerCase().includes('person1') ? 'p1' : speaker.toLowerCase().includes('person2') ? 'p2' : 'p3'}`;
    }
    if (this.hudBudget) this.hudBudget.textContent = budget;
    if (this.hudScene) this.hudScene.textContent = scene;
  }

  /**
   * Resets and restarts the countdown timer for the active slide.
   */
  resetSlideTimer(slide) {
    if (this.timerInterval) clearInterval(this.timerInterval);

    this.slideTimeBudget = parseInt(slide.dataset.timeBudget, 10) || 120;
    this.slideSecondsRemaining = this.slideTimeBudget;
    this.isTimerPaused = false;
    this.updateSlideTimerDisplay();

    this.timerInterval = setInterval(() => {
      if (!this.isTimerPaused) {
        this.slideSecondsRemaining--;
        this.updateSlideTimerDisplay();
      }
    }, 1000);
  }

  /**
   * Formats and updates slide timer display in MM:SS.
   */
  updateSlideTimerDisplay() {
    if (!this.hudSlideTimer) return;

    const isOvertime = this.slideSecondsRemaining < 0;
    const absSeconds = Math.abs(this.slideSecondsRemaining);
    const mins = Math.floor(absSeconds / 60);
    const secs = absSeconds % 60;
    const formatted = `${isOvertime ? '-' : ''}${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

    this.hudSlideTimer.textContent = formatted;
    if (isOvertime) {
      this.hudSlideTimer.classList.add('overtime');
    } else {
      this.hudSlideTimer.classList.remove('overtime');
    }
  }

  /**
   * Master 45-minute cumulative presentation clock.
   */
  startPresentationClock() {
    if (this.presentationInterval) clearInterval(this.presentationInterval);

    this.presentationInterval = setInterval(() => {
      this.presentationElapsedSeconds++;
      if (this.hudElapsed) {
        const mins = Math.floor(this.presentationElapsedSeconds / 60);
        const secs = this.presentationElapsedSeconds % 60;
        this.hudElapsed.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
      }
    }, 1000);
  }

  /**
   * Video Playback Manager: smooth playback on slide entry.
   */
  handleVideoEnter(slide) {
    const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
    if (!video) return;

    video.currentTime = 0;

    // Support slides that start in a paused initial state (e.g. Slide 1 Step 0)
    if (slide.dataset.pauseOnEntry === 'true' && this.currentFragmentIndex < 0) {
      video.pause();
      video.classList.add('loaded', 'playing');
      return;
    }

    const playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise
        .then(() => {
          video.classList.add('playing');
        })
        .catch((err) => {
          // Graceful fallback: If MP4 is missing or autoplay prevented, show minimal TeX fallback
          video.classList.remove('playing');
        });
    }
  }

  /**
   * Video Pause on slide exit.
   */
  handleVideoExit(slide) {
    const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
    if (video) {
      video.pause();
    }
  }

  /**
   * Asynchronous Preload Manager: buffers next slide's video.
   */
  preloadNextVideo(nextIndex) {
    if (nextIndex >= this.totalSlides) return;
    const nextSlide = this.slides[nextIndex];
    const nextVideo = nextSlide.querySelector('video.stage-video') || nextSlide.querySelector('video');
    if (!nextVideo) return;

    const source = nextVideo.querySelector('source');
    const src = source ? source.getAttribute('src') : nextVideo.getAttribute('src');
    if (!src) return;

    if (!this.videoPreloadCache.has(src)) {
      const preloadLink = document.createElement('link');
      preloadLink.rel = 'preload';
      preloadLink.as = 'video';
      preloadLink.href = src;
      document.head.appendChild(preloadLink);
      this.videoPreloadCache.set(src, true);
    }
  }

  /**
   * Dispatches custom event for Phase 4 WebSocket Companion.
   */
  dispatchSlideChangeEvent(slide, totalFragments = 0) {
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

    const event = new CustomEvent('slidechange', { detail: payload });
    window.dispatchEvent(event);

    console.log(`[SRS Engine] -> Slide ${payload.slideNum} (${payload.slideId}) | ${payload.manimScene} | Speaker: ${payload.speaker}`);

    if (window.SRS_SOCKET && window.SRS_SOCKET.readyState === WebSocket.OPEN) {
      window.SRS_SOCKET.send(JSON.stringify({ type: 'SLIDE_CHANGE', data: payload }));
    }
  }

  /**
   * Toggles fullscreen presentation mode.
   */
  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch((err) => {
        console.warn(`Fullscreen request failed: ${err.message}`);
      });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }
}

// Global initialization on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.srsPresentation = new PresentationController();
});
