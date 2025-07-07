# hello_gravity_circuit_controller.py
# Magnetic Lift Coil Demo – ZPENS-Inspired

import time
import RPi.GPIO as GPIO  # Use 'machine' if adapting for MicroPython

# --- CONFIGURABLE SETTINGS ---
COIL_PIN = 18           # GPIO pin connected to coil switch transistor
PWM_FREQ = 1000         # PWM frequency in Hz
DUTY_CYCLE = 75         # % of power sent to coil (tune this)
ON_DURATION = 0.2       # Coil pulse duration in seconds
OFF_DURATION = 0.5      # Delay between pulses in seconds

# --- GPIO SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(COIL_PIN, GPIO.OUT)
coil_pwm = GPIO.PWM(COIL_PIN, PWM_FREQ)
coil_pwm.start(0)

print("[STARTING] Hello Gravity Demo - Magnetic Lift Coil")

try:
    while True:
        print("[PULSE] Activating Coil")
        coil_pwm.ChangeDutyCycle(DUTY_CYCLE)
        time.sleep(ON_DURATION)

        print("[WAIT] Coil resting")
        coil_pwm.ChangeDutyCycle(0)
        time.sleep(OFF_DURATION)

except KeyboardInterrupt:
    print("[SHUTDOWN] Demo ending...")

finally:
    coil_pwm.stop()
    GPIO.cleanup()
    print("[CLEAN] GPIO cleared. Goodbye.")
