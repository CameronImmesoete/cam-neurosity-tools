# Code Review Standards

> Base review standards: [CameronImmesoete/.github/.github/copilot-review-skill.md@1f79bfb](https://github.com/CameronImmesoete/.github/blob/1f79bfb3e9eee277d05ecdd3332220204cb0f38b/.github/copilot-review-skill.md)

## Repository-Specific Review Criteria

### Signal Processing
- Are EEG frequency bands (delta, theta, alpha, beta, gamma) correctly defined?
- Is windowing applied before FFT (Hanning, Hamming)?
- Are filter parameters documented (cutoff frequency, order, type)?
- Is the sampling rate accounted for in all frequency calculations?

### Data Stream Handling
- Are RxJS subscriptions properly cleaned up (unsubscribe on teardown)?
- Is backpressure handled for high-frequency EEG streams?
- Are stream errors caught and surfaced, not silently swallowed?
- Is there reconnection logic for dropped Bluetooth/USB connections?

### Device Reconnect
- Does the code handle device disconnection gracefully?
- Is there exponential backoff on reconnect attempts?
- Are users notified of connection state changes?
- Does the code avoid busy-loop polling for device status?

### Brain Data Privacy
- Is EEG data treated as PII/biometric data?
- Are raw brain recordings excluded from version control?
- Is subject-identifiable data stripped before export or logging?
- Is cloud transmission of brain data gated on explicit user consent?
