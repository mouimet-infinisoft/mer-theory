#!/usr/bin/env python3
"""Figure generation scripts for MER Theory paper.
Generates reproducible figures into the specified output directory.
Requires: numpy, matplotlib
"""
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'figure.dpi': 150, 'savefig.dpi': 300})


def ensure_outdir(outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)


def generate_lemniscate(path: Path, a=1.0, n=2048):
    t = np.linspace(0, 2 * np.pi, n)
    r = a * np.sqrt(2) * np.cos(t) / (np.sin(t) ** 2 + 1)
    x = r * np.cos(t)
    y = r * np.sin(t)
    plt.figure(figsize=(4, 4))
    plt.plot(x, y, color='#1f77b4', lw=1)
    plt.axis('equal')
    plt.axis('off')
    plt.title('MER Lemniscate (schematic)')
    plt.savefig(path, bbox_inches='tight', pad_inches=0.1)
    plt.close()


def generate_fibonacci_spiral(path: Path, n=12):
    # Simple discrete Fibonacci spiral using quarter-circle arcs
    phi = (1 + 5 ** 0.5) / 2
    theta = np.linspace(0, 4 * np.pi, 1024)
    r = (phi ** (theta / (2 * np.pi))) * 0.05
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.figure(figsize=(4, 4))
    plt.plot(x, y, lw=1.2, color='#ff7f0e')
    plt.axis('equal')
    plt.axis('off')
    plt.title('Fibonacci Spiral (schematic)')
    plt.savefig(path, bbox_inches='tight', pad_inches=0.1)
    plt.close()


def generate_mandelbrot(path: Path, w=800, h=600, maxiter=200):
    x = np.linspace(-2.5, 1.0, w)
    y = np.linspace(-1.25, 1.25, h)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    output = np.zeros(C.shape, dtype=int)
    for i in range(maxiter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        output[mask & (np.abs(Z) > 2)] = i
    plt.figure(figsize=(6, 4.5))
    plt.imshow(output, cmap='magma', extent=[x[0], x[-1], y[0], y[-1]])
    plt.axis('off')
    plt.title('Mandelbrot Set (detail)')
    plt.savefig(path, bbox_inches='tight', pad_inches=0.1)
    plt.close()


def generate_all(outdir: Path):
    ensure_outdir(outdir)
    generate_lemniscate(outdir / 'lemniscate.png')
    generate_fibonacci_spiral(outdir / 'fibonacci_spiral.png')
    generate_mandelbrot(outdir / 'mandelbrot.png')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate paper figures')
    parser.add_argument('outdir', nargs='?', default='paper/images', help='Output directory')
    args = parser.parse_args()
    generate_all(Path(args.outdir))
