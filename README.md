# security-lab

# AuRA Security Lab

A dedicated test repository for validating AuRA security scanning and
business risk scoring.

## Security checks

- SCA: OSV checks dependency versions for known vulnerabilities.
- SAST: GitHub CodeQL analyzes Python source code.
- Risk scoring: AuRA combines scanner findings into a repository risk assessment.

## Test files

- `requirements.txt`: intentionally outdated dependency for SCA testing.
- `app.py`: intentionally vulnerable SQL query for CodeQL testing.
- `.github/workflows/codeql.yml`: automated CodeQL workflow.

## Safety

This repository contains intentionally vulnerable examples for controlled
security testing. Do not reuse them in production applications.

## Expected validation

1. OSV should be queried for the pinned dependency.
2. CodeQL should analyze the Python source.
3. AuRA should consume the findings actually returned by each scanner.
4. The business risk score should be calculated from those findings.
