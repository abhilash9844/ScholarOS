# Unreleased

## Added

- Introduced a dedicated Technical Term Extraction stage.
- Added transcript preprocessing module.
- Added initial deterministic vocabulary-based extractor.
- Separated concept extraction from concept organization.

## Changed

- Refactored ScholarOS toward a modular pipeline:
  Transcript → Preprocessor → Term Extraction → Concept Inventory → Notes.

## Known Issues

- Technical term extraction currently misses many concepts.
- Transcript preprocessing requires redesign.
- No transcript caching; repeated YouTube requests can trigger rate limits.
- Concept inventory quality depends on extractor output.