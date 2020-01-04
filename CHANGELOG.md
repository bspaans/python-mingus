## [0.6.0] - 2020-01-04

This is the first official release to support **Python 3** (≥ 3.5).  I've tried not to break Python 2 compatibility, but I'm **officially not supporting Python 2.7** any further, especially since its end-of-life has come.

Some other changes — both old, that had been merged but not released, and new — are also part of this release:

### Added
* (#12) Add `channel` and `velocity` properties and setters to Note
* (#18) Update LilyPond.from_Bar to handle minor, flat and sharp keys
* Better documentation for developers and standardization of the development environment

### Changed
* (#42) Fix: 3/x (3/8, 3/16, etc.) are not compound meters

### Fixed
* (#11) Documentation fixes
* (#14) Fix LilyPond filename extension detection
