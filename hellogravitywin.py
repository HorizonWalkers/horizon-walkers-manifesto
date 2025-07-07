import time

# --- MOCK GPIO MODULE (FOR WINDOWS) ---
class MockPWM:
    def __init__(self, pin, freq):
        self.pin = pin
        self.freq = freq
    def start(self, duty):
        print(f"[MOCK] PWM started on pin {self.pin} at {self.freq}Hz, duty {duty}%")
    def ChangeDutyCycle(self, duty):
        print(f"[MOCK] PWM duty cycle changed to {duty}%")
    def stop(self):
        print(f"[MOCK] PWM stopped")

class MockGPIO:
    BCM = "BCM"
    OUT = "OUT"
    def setmode(self, mode):
        print(f"[MOCK] GPIO mode set to {mode}")
    def setup(self, pin, mode):
        print(f"[MOCK] Pin {pin} set to mode {mode}")
    def PWM(self, pin, freq):
        return MockPWM(pin, freq)
    def cleanup(self):
        print(f"[MOCK] GPIO cleaned up")

GPIO = MockGPIO()

# --- CONFIGURABLE SETTINGS ---
COIL_PIN = 18
PWM_FREQ = 1000
DUTY_CYCLE = 75
ON_DURATION = 0.2
OFF_DURATION = 0.5

# --- SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(COIL_PIN, GPIO.OUT)
coil_pwm = GPIO.PWM(COIL_PIN, PWM_FREQ)
coil_pwm.start(0)

print("[STARTING] Hello Gravity Demo (Mock)")

try:
    while True:
        print("[PULSE] Activating Coil")
        coil_pwm.ChangeDutyCycle(DUTY_CYCLE)
        time.sleep(ON_DURATION)

        print("[WAIT] Coil resting")
        coil_pwm.ChangeDutyCycle(0)
        time.sleep(OFF_DURATION)

except KeyboardInterrupt:
    print("[SHUTDOWN] Ending Mock Session")

finally:
    coil_pwm.stop()
    GPIO.cleanup()
    print("[CLEAN] Goodbye from Mock GPIO")
