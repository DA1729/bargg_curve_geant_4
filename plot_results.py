import subprocess
import re
import matplotlib.pyplot as plt
def run_simulation():
    process = subprocess.Popen(['./build/bragg_curve', 'run1.mac'], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT, 
                               text=True)
    depths = []
    edeps = []
    for line in process.stdout:
        match = re.search(r'depth: ([\d\.]+) mm, edep: ([\d\.]+) keV/event', line)
        if match:
            depths.append(float(match.group(1)))
            edeps.append(float(match.group(2)))
    process.wait()
    return depths, edeps
def plot(depths, edeps):
    plt.figure(figsize=(10, 6))
    plt.plot(depths, edeps, 'b-')
    plt.xlabel('Depth (mm)')
    plt.ylabel('Energy Deposition (keV/event)')
    plt.title('Bragg Curve in Argon Gas')
    plt.grid(True)
    plt.savefig('bragg_curve.png')
if __name__ == "__main__":
    depths, edeps = run_simulation()
    if depths:
        plot(depths, edeps)
