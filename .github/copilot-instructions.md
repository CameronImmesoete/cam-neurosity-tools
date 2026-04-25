# Copilot Instructions

> Base instructions: [CameronImmesoete/.github/.github/copilot-instructions.md@1f79bfb](https://github.com/CameronImmesoete/.github/blob/1f79bfb3e9eee277d05ecdd3332220204cb0f38b/.github/copilot-instructions.md)

## Repository-Specific Guidelines

### Neurosity SDK
- Use the `@neurosity/sdk` package for all device interactions
- Always check device connection status before initiating data streams
- Handle SDK initialization errors gracefully (missing credentials, network timeouts)
- Use `neurosity.calm()`, `neurosity.focus()`, and `neurosity.brainwaves()` observables with proper RxJS subscription cleanup

### EEG Data Streams
- Always unsubscribe from brainwave observables when components unmount or scripts exit
- Buffer EEG samples appropriately (default 256Hz sample rate, ~16 samples per epoch)
- Validate electrode impedance before trusting signal quality
- Handle stream interruptions with automatic reconnection logic
- Never log raw EEG data to console in production (volume and privacy concerns)

### Brain Data Privacy
- EEG data is biometric and personally identifiable. Treat it as PII.
- Never commit raw EEG recordings, training data, or user brain profiles
- Strip subject identifiers before any data export or visualization
- Store brain data locally by default. Cloud sync only with explicit user consent.
- Add `.neurosity/` and `*.csv` (raw EEG exports) to `.gitignore`

### Device Lifecycle
- Crown device has limited battery. Avoid polling loops; prefer event-driven patterns.
- Handle device sleep/wake transitions in long-running scripts
- Test with both USB and Bluetooth connection modes
- Gracefully degrade when device is unavailable (offline mode for cached models)
