# 8-language project submission

## Overview
This repository contains C++ sources used for competitive programming and algorithm experimentation.

- `y.cpp`: A complete, compilable solution that processes multiple test cases. For each test case, it reads an integer `n` and an array of `n` integers, then computes the maximum count of elements that can be kept under a specific difference constraint (common CF-style problem). It outputs one integer per test case.
- `xx.cpp`: A scratch/utility playground containing assorted helpers (power, factorial, prime check, gcd/lcm, etc.). It is not intended for compilation in its current form.

## Project structure
- `y.cpp` — main solution (compiles and runs)
- `xx.cpp` — scratch utilities (do not compile as-is)
- `README.md` — this file

## Requirements
- GCC or Clang with C++17 support
  - Recommended: `g++ (>= 9)` or `clang++ (>= 10)`
- A POSIX-like shell (Linux/macOS; Windows via WSL)

## Build
Build the runnable program from `y.cpp`:

```bash
# From the repository root
g++ -std=c++17 -O2 -pipe -march=native -o y y.cpp
```

If you prefer Clang:

```bash
clang++ -std=c++17 -O2 -pipe -march=native -o y y.cpp
```

Note: Do not attempt to build `xx.cpp` in its current form; it contains stray content meant for scratch use and will not compile.

## Run
`y` reads from standard input and writes to standard output.

Input format (per the current implementation in `y.cpp`):
- First line: integer `t` — number of test cases
- For each test case:
  - line with integer `n`
  - line with `n` integers (can be negative, zero, or positive)

Example:

```bash
# Example with a single test case
printf "1\n5\n-1 -2 3 4 5\n" | ./y
```

The program prints a single integer per test case, representing the maximal count under the implemented constraints.

## Notes
- `y.cpp` uses common CP conveniences like `#include <bits/stdc++.h>` and `#define int long long`. For production use, consider replacing these with explicit includes and types.
- If you hit issues with `-march=native` on older toolchains or CI, remove it.

## License
MIT (or your preferred license)
