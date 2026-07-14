# Source Tree Analysis

## Product and project files

```text
srvls/
├── srvls                         # Executable Python product and sole runtime entry point
├── README.md                    # Current srvls user and operations documentation
├── tests/
│   └── test_smoke.sh            # Live-host end-to-end smoke and injection regression test
├── mise.toml                    # Environment hooks and test/version task definitions
├── .mise/
│   ├── scripts/
│   │   ├── link-agentfiles.sh   # Maintains CLAUDE.md/GEMINI.md links to AGENTS.md
│   │   └── versioning.sh        # Generic multi-format semantic-version helper
│   └── version-files.conf       # Version manifest; currently Git tags only
├── .project.json                # srvls/Plane project metadata
├── .copier-answers.yml          # CommonProject template provenance and srvls identity
├── .env.op                      # 1Password reference template; contains no resolved secret
├── .gitignore                   # Secret, generated-output, bytecode, and artifact exclusions
├── AGENTS.md                    # Repository-local orchestration instructions
├── LICENSE                      # MIT license
├── tasks.md                     # Active orchestration ledger
└── docs/                        # BMAD project knowledge and resumable scan state
```

## Generated and operational metadata

```text
├── _bmad/                       # Installed BMAD framework; not product runtime
├── .agents/                     # Agent skill installation; not product runtime
├── .claude/                     # Generated Claude-facing skill mirror
├── .opencode/commands/          # Generated OpenCode command mirror
└── .git/                        # Active Git repository
```

The generated skill trees are large but do not make this a monorepo. The product remains a one-file CLI.

## Entry and integration points

- Runtime entry: `srvls:main()`.
- Development entry: `mise run test` or `bash tests/test_smoke.sh`.
- Installation entry: symlink `srvls` into a directory on `PATH`.
- Secret materialization: mise enter hook runs `op inject -i .env.op > .env`.
- Host reads: crontab commands, `/etc/crontab`, `/etc/cron.d`, systemd, Docker, and PM2.
- Host writes/mutations: only explicit lifecycle subcommands and fzf keybindings.
- Export integration: shell redirection to JSON, Prometheus textfile, or Markdown files.

## Organization assessment

The flat product layout is proportionate to 364 lines of Python. If the CLI grows, the first natural boundaries are `collectors`, `renderers`, `actions`, and `models`; splitting solely for style would currently add more packaging overhead than value.
