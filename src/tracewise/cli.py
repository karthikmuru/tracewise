"""Command-line interface for tracewise."""

from __future__ import annotations

import argparse
from typing import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tracewise",
        description="Analyze MySQL slow query logs and rank query hotspots.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze = subparsers.add_parser(
        "analyze",
        help="Analyze a MySQL slow query log.",
    )
    analyze.add_argument(
        "--input",
        required=True,
        help="Path to a MySQL slow query log file.",
    )
    analyze.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format.",
    )
    analyze.add_argument(
        "--top",
        type=int,
        default=10,
        help="Limit to the top N queries.",
    )
    analyze.add_argument(
        "--min-time",
        type=float,
        default=0.0,
        help="Minimum Query_time (seconds) to include.",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "analyze":
        # Stub implementation for the initial CLI scaffold.
        print(
            "tracewise analyze (stub): input={input} format={format} top={top} min_time={min_time}".format(
                input=args.input,
                format=args.format,
                top=args.top,
                min_time=args.min_time,
            )
        )
        return 0

    parser.error("Unknown command")
    return 2
