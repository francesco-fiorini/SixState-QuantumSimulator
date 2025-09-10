# Qiskit Implementation of the Six-State Quantum Key Distribution Protocol under Partial Intercept-Resend Attack  

This repository contains a Qiskit-based implementation of the **Six-State quantum key distribution (QKD) protocol** under a **partial intercept-resend eavesdropping attack**.  
Compared to BB84, the Six-State protocol extends the measurement basis choices from two to three, providing a stronger resilience against eavesdropping strategies and enabling a more accurate estimation of the quantum bit error rate (QBER).  

The simulation also integrates **channel noise**, modeled through the readout error probability of the receiver backends used. From the observed QBER, the implementation estimates the interception density while accounting for the intrinsic noise of the quantum channel.  
In addition, performance metrics are exported to an automatically generated and continuously updated **Excel file** for further analysis.  

This project aims to support research and development of **intrusion detection mechanisms** in quantum communication, leveraging the increased robustness of the Six-State protocol.  

---

## Table of Contents
- [Introduction](#introduction)
- [Installation and Usage](#installation-and-usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
Quantum Key Distribution (QKD) is a powerful method that leverages the principles of quantum mechanics to ensure unconditionally secure communication.  
The **Six-State protocol** is a natural generalization of the BB84 protocol, employing three mutually unbiased bases (X, Y, Z) instead of just two. This feature makes it more robust to eavesdropping attacks such as intercept-resend, at the cost of a slightly reduced efficiency in key generation.  

This implementation demonstrates:  
1. How QKD is affected by a partial intercept-resend attack.  
2. The effect of realistic channel noise on the QBER and key security.  
3. A method to estimate the interception density based on QBER data corrected for noise.  

---

## Installation and Usage
The implementation builds upon the **quantum-solver** library by Daniel Escanez-Exposito, available at [https://github.com/jdanielescanez/quantum-solver](https://github.com/jdanielescanez/quantum-solver).  

To use this package:  
1. Clone or download the `quantum-solver` repository.  
2. Replace the `six_state` folder under `quantum-solver/src/crypto` with the current `six_state` package.  
3. Run the simulation with:  
`python3 __main__.py`

Ensure that Qiskit and other dependencies specified in the quantum-solver repository are installed.

## Features

1) Full implementation of the Six-State QKD protocol
2) Simulation of partial intercept-resend eavesdropping attacks
3) Realistic modeling of channel noise with receiver backend readout error probabilities
4) Calculation of Quantum Bit Error Rate (QBER) for sender-receiver key comparison
5) Estimation of eavesdropping interception density, adjusted for channel noise
6) Automated generation of Excel reports for performance metrics
7) Detailed execution time and resource usage analysis
8) Support for customizable backend configurations

## Contributing
We welcome contributions to improve this project! For suggestions or issues, please contact francesco.fiorini@phd.unipi.it.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
