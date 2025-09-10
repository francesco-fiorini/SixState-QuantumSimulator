from abc import ABC, abstractmethod
from qiskit import QuantumCircuit
from qiskit.circuit.library import YGate, ZGate
from qiskit.circuit.gate import Gate
import qiskit.quantum_info as qi
from numpy.random import randint
import numpy as np
from math import ceil

class Partecipant(ABC):
  ## Constructor
  @abstractmethod
  def __init__(self, name='', original_bits_size=0):
    ## The name of the participant
    self.name = name
    ## The original size of the message
    self.original_bits_size = original_bits_size
    ## The values of the participant
    self.values = None
    ## The axes of the participant
    self.axes = None
    ## The key of the participant
    self.key = None
    ## If the key is determined safe
    self.is_safe_key = False
    ## The otp of the participant
    self.otp = None
    ## The gate measuring z and y axes
    self.set_hy()

  ## Values setter
  def set_values(self, values=None):
    if values == None:
      self.values = list(randint(2, size=self.original_bits_size,dtype=int))
    else:
      self.values = values

  ## Axes setter
  def set_axes(self, axes=None):
    if axes == None:
      self.axes = list(randint(3, size=self.original_bits_size,dtype=int))
    else:
      self.axes = axes

  ## Print values
  def show_values(self):
    print('\n' + self.name, 'Values:')
    print(self.values)
    return self.values

  ## Print axes
  def show_axes(self):
    print('\n' + self.name, 'Axes:')
    print(self.axes)
    return self.axes
  
  ## Print key
  def show_key(self):
    print('\n' + self.name, 'Key:')
    print(self.key)
    return self.key

  ## Print otp
  def show_otp(self):
    print('\n' + self.name, 'OTP:')
    print(self.otp)
    return self.otp

  ## Remove the values of the qubits that were measured on the wrong axis
  def remove_garbage(self, another_axes):
    self.key = []
    for i in range(self.original_bits_size):
      if self.axes[i] == another_axes[i]:
        self.key.append(self.values[i])

  ## Check if the shared key is equal to the current key
  def check_key(self, shared_key):
    return shared_key == self.key[:len(shared_key)]

  ## Use the rest of the key and validate it
  def confirm_key(self, shared_size):
    self.key = self.key[shared_size:]
    self.is_safe_key = True

  ## Generate an One-Time Pad
  def generate_otp(self, n_bits):
    self.otp = []
    for i in range(ceil(len(self.key) / n_bits)):
      bits_string = ''.join(map(str, self.key[i * n_bits: (i + 1) * n_bits]))
      self.otp.append(int(bits_string, 2))

  ## Performs an XOR operation between the message and the One-Time Pad
  def xor_otp_message(self, message):
    final_message = ''
    CHR_LIMIT = 1114112
    if len(self.otp) > 0:
      for i, char in enumerate(message):
        final_message += chr((ord(char) ^ self.otp[i % len(self.otp)]) % CHR_LIMIT)
    return final_message

  ## New gate setter
  def set_hy(self):
    hy_op = qi.Operator(1/np.sqrt(2)*(YGate().to_matrix() + ZGate().to_matrix()))
    hy_gate = QuantumCircuit(1)
    hy_gate.unitary(hy_op, [0], label='h_y')
    self.hy = hy_gate.to_gate()

