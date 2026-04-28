# Security Policy

## Supported Versions

The latest tagged release and the `main` branch receive security fixes.

## Reporting a Vulnerability

Please report suspected security issues privately through GitHub Security Advisories when the repository is public. If advisories are not available, open an issue with minimal detail and ask for a private contact path.

Do not include secrets, private repository content, or sensitive logs in a public issue.

## Scope

This repository is a text-based agent skill. Security-relevant reports usually involve:

- instructions that could cause an agent to expose secrets
- unsafe guidance for destructive repository operations
- hidden network, credential, or exfiltration behavior in bundled scripts
- misleading installation or release instructions

The project should remain free of runtime credential requirements.
