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

    // Minimal Floating Deck Status HUD (65" TV Minimalist Indicator)
    this.deckStatus = document.getElementById('deck-status');
    this.speakerBadge = document.getElementById('speaker-badge');
    this.slideCounter = document.getElementById('slide-counter');

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
      const videos = slide.querySelectorAll('video');
      videos.forEach((video) => {
        video.addEventListener('canplay', () => video.classList.add('loaded'));
        video.addEventListener('playing', () => video.classList.add('playing'));
        video.addEventListener('error', () => video.classList.remove('playing', 'loaded'));
      });
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
   * Advances forward: either reveals next fragment/step, or advances to next slide.
   */
  next() {
    const currentSlide = this.slides[this.currentSlideIndex];
    const steps = Array.from(currentSlide.querySelectorAll('.fragment, .step'));

    if (this.currentFragmentIndex < steps.length - 1) {
      this.currentFragmentIndex++;
      this.revealFragment(steps, this.currentFragmentIndex);
    } else {
      if (this.currentSlideIndex < this.totalSlides - 1) {
        this.goToSlide(this.currentSlideIndex + 1);
      }
    }
  }

  /**
   * Reverses backward: either hides previous fragment/step, or jumps to previous slide.
   */
  prev() {
    const currentSlide = this.slides[this.currentSlideIndex];
    const steps = Array.from(currentSlide.querySelectorAll('.fragment, .step'));

    if (this.currentFragmentIndex >= 0) {
      this.hideFragment(steps, this.currentFragmentIndex);
      this.currentFragmentIndex--;
    } else {
      if (this.currentSlideIndex > 0) {
        this.goToSlide(this.currentSlideIndex - 1, true);
      }
    }
  }

  /**
   * Reveals a specific fragment or controllable step.
   */
  revealFragment(steps, index) {
    const step = steps[index];
    if (!step) return;

    step.classList.add('visible');
    const slide = this.slides[this.currentSlideIndex];

    // Cuepoint video stepping
    if (slide.dataset.cuepoints) {
      const cuepoints = slide.dataset.cuepoints.split(',').map(s => parseFloat(s.trim()));
      const targetTime = cuepoints[index + 1];
      const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
      if (video && targetTime !== undefined) {
        this.playVideoToCuepoint(video, targetTime);
      }
    }

    if (step.dataset.videoAction === 'next-segment') {
      const seg1 = slide.querySelector('.stage-video-seg1');
      const seg2 = slide.querySelector('.stage-video-seg2');
      if (seg1 && seg2) {
        seg1.pause();
        seg1.style.opacity = '0';
        seg1.style.pointerEvents = 'none';
        seg2.style.opacity = '1';
        seg2.style.pointerEvents = 'auto';
        seg2.currentTime = 0;
        seg2.play().catch(() => {});
      }
    } else if (step.dataset.videoAction === 'resume') {
      const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
      if (video) video.play();
    }
  }

  /**
   * Hides a specific fragment or controllable step.
   */
  hideFragment(steps, index) {
    const step = steps[index];
    if (!step) return;

    step.classList.remove('visible');
    const slide = this.slides[this.currentSlideIndex];

    // Cuepoint video reversing
    if (slide.dataset.cuepoints) {
      const cuepoints = slide.dataset.cuepoints.split(',').map(s => parseFloat(s.trim()));
      const targetTime = cuepoints[index];
      const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
      if (video && targetTime !== undefined) {
        this.seekVideoTo(video, targetTime);
      }
    }

    if (step.dataset.videoAction === 'next-segment') {
      const seg1 = slide.querySelector('.stage-video-seg1');
      const seg2 = slide.querySelector('.stage-video-seg2');
      if (seg1 && seg2) {
        seg2.pause();
        seg2.currentTime = 0;
        seg2.style.opacity = '0';
        seg2.style.pointerEvents = 'none';
        seg1.style.opacity = '1';
        seg1.style.pointerEvents = 'auto';
      }
    } else if (step.dataset.videoAction === 'resume') {
      const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
      if (video) {
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

    // Manage fragments and steps
    const steps = Array.from(newSlide.querySelectorAll('.fragment, .step'));
    if (showAllFragments) {
      steps.forEach(f => f.classList.add('visible'));
      this.currentFragmentIndex = steps.length - 1;
    } else {
      steps.forEach(f => f.classList.remove('visible'));
      this.currentFragmentIndex = -1;
    }

    // Update telemetry, timers, and HUD
    this.updateHUD(newSlide);
    this.resetSlideTimer(newSlide);
    this.handleVideoEnter(newSlide, showAllFragments);
    this.preloadNextVideo(targetIndex + 1);

    // Dispatch Phase 4 Companion Hook
    this.dispatchSlideChangeEvent(newSlide, steps.length);
  }

  /**
   * Updates hidden presenter rehearsal HUD metrics and minimalist on-screen indicator.
   */
  updateHUD(slide) {
    // 1. Update Minimal Floating Deck Status Indicator (65" TV / 6-Meter Readability)
    if (this.speakerBadge || this.slideCounter) {
      const speakerAttr = (slide.dataset.speaker || '').toLowerCase();
      let presenterName = 'A. Navid';
      if (speakerAttr.includes('person2') || (this.currentSlideIndex >= 10 && this.currentSlideIndex <= 16)) {
        presenterName = 'S. Asadi';
      } else if (speakerAttr.includes('person3') || this.currentSlideIndex >= 17) {
        presenterName = 'S. Sharifi';
      } else {
        presenterName = 'A. Navid';
      }

      const currentNum = String(this.currentSlideIndex + 1).padStart(2, '0');
      const totalNum = String(this.totalSlides).padStart(2, '0');

      if (this.speakerBadge) this.speakerBadge.textContent = presenterName;
      if (this.slideCounter) this.slideCounter.textContent = `${currentNum} / ${totalNum}`;
    }

    // 2. Update Hidden Rehearsal HUD (Toggled via 'H')
    if (!this.hud) return;

    const slideNum = slide.dataset.slideNum || String(this.currentSlideIndex + 1);
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
  handleVideoEnter(slide, isBackward = false) {
    // Multi-segment video slide (e.g. Slide 1: Seg 1 then Seg 2)
    if (slide.dataset.multiSegment === 'true') {
      const seg1 = slide.querySelector('.stage-video-seg1');
      const seg2 = slide.querySelector('.stage-video-seg2');
      if (seg1 && seg2) {
        if (this.currentFragmentIndex < 0) {
          seg2.pause();
          seg2.currentTime = 0;
          seg2.style.opacity = '0';
          seg2.style.pointerEvents = 'none';
          seg1.style.opacity = '1';
          seg1.style.pointerEvents = 'auto';
          seg1.currentTime = 0;
          const playPromise = seg1.play();
          if (playPromise !== undefined) {
            playPromise.then(() => seg1.classList.add('playing')).catch(() => {});
          }
        } else {
          seg1.pause();
          seg1.style.opacity = '0';
          seg1.style.pointerEvents = 'none';
          seg2.style.opacity = '1';
          seg2.style.pointerEvents = 'auto';
          const playPromise = seg2.play();
          if (playPromise !== undefined) {
            playPromise.then(() => seg2.classList.add('playing')).catch(() => {});
          }
        }
      }
      return;
    }

    const video = slide.querySelector('video.stage-video') || slide.querySelector('video');
    if (!video) return;

    // Slide with frame-accurate cuepoints
    if (slide.dataset.cuepoints) {
      const cuepoints = slide.dataset.cuepoints.split(',').map(s => parseFloat(s.trim()));
      if (isBackward) {
        const lastCue = cuepoints[cuepoints.length - 1];
        this.seekVideoTo(video, lastCue);
        video.classList.add('loaded', 'playing');
      } else {
        video.currentTime = 0;
        video.classList.add('loaded', 'playing');
        this.playVideoToCuepoint(video, cuepoints[0]);
      }
      return;
    }

    video.currentTime = 0;

    // Support slides that start in a paused initial state
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
   * Play video up to a target cuepoint time and pause exactly there.
   */
  playVideoToCuepoint(video, targetTime) {
    if (!video) return;

    if (video._rafId) {
      if ('cancelVideoFrameCallback' in video) {
        video.cancelVideoFrameCallback(video._rafId);
      } else {
        cancelAnimationFrame(video._rafId);
      }
      video._rafId = null;
    }

    const checkTime = () => {
      if (video.paused) return;
      if (video.currentTime >= targetTime - 0.02) {
        video.pause();
        video.currentTime = targetTime;
        video._rafId = null;
        return;
      }
      if ('requestVideoFrameCallback' in video) {
        video._rafId = video.requestVideoFrameCallback(checkTime);
      } else {
        video._rafId = requestAnimationFrame(checkTime);
      }
    };

    const playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise
        .then(() => {
          video.classList.add('playing');
          if ('requestVideoFrameCallback' in video) {
            video._rafId = video.requestVideoFrameCallback(checkTime);
          } else {
            video._rafId = requestAnimationFrame(checkTime);
          }
        })
        .catch(console.warn);
    }
  }

  /**
   * Seek video immediately to a specific timestamp and pause.
   */
  seekVideoTo(video, targetTime) {
    if (!video) return;
    if (video._rafId) {
      if ('cancelVideoFrameCallback' in video) {
        video.cancelVideoFrameCallback(video._rafId);
      } else {
        cancelAnimationFrame(video._rafId);
      }
      video._rafId = null;
    }
    video.pause();
    video.currentTime = targetTime;
  }

  /**
   * Video Pause on slide exit.
   */
  handleVideoExit(slide) {
    const videos = slide.querySelectorAll('video');
    videos.forEach(v => {
      if (v._rafId) {
        if ('cancelVideoFrameCallback' in v) {
          v.cancelVideoFrameCallback(v._rafId);
        } else {
          cancelAnimationFrame(v._rafId);
        }
        v._rafId = null;
      }
      v.pause();
    });
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
