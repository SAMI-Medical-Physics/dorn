# Change Log
All notable changes to this project will be documented in this file.

## [1.9.2] - 2022-01-02

### Added
- Hints in green text, based on feedback from new technologist users:
  - Letter case used in patient name appears in reports
  - 24-hour time

### Fixed
- Forget previous filename when a new patient is started in the same run.

## [1.9.3] - 2022-02-04

### Changed
- Executable uses `glowgeeen` 0.0.2 (from 0.0.1).
- Restrictions with dose constraints that are per treatment episode are shown in blue text.

## [1.9.4] - 2022-02-23

### Fixed
- In the restriction tables in reports, some of the new restriction names were long and went onto a second line, 
causing the columns to not be aligned. The columns now stay aligned.

## [1.9.5] - 2022-10-11

### Changed
- Executable uses `glowgreen` 0.0.4.
- Restrictions begin unticked.
- For the curve fit, the initial guess for the clearance component half-life or -lives is a third of the physical half life.
- Increased font size in patient hand out.

## [1.9.6] - 2022-10-19

### Added
- Starting from this version, the Github release includes a standalone executable of the Dorn program built on Windows and using the latest version of the `glowgreen` package.
