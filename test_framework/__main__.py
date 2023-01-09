"""Entry point for test_framework."""
try:
    from .cli import main  # pragma: no cover
except:
    from cli import main

if __name__ == "__main__":  # pragma: no cover
    main()
