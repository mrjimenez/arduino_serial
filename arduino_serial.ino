#define DEBUG 0

const uint16_t MAX_BUFFER_SIZE = SERIAL_RX_BUFFER_SIZE - 1;
const uint32_t BLOCK_SIZE = 32 * 1024L;
uint16_t buffer_size = 0;
uint32_t threshold = 0;

void setup()
{
	Serial.begin(115200);
	while (!Serial) {
		; // wait for serial port to connect. Needed for Leonardo only
	}
	Serial.print(F("!Maximum serial buffer size: "));
	Serial.println(MAX_BUFFER_SIZE);
}

void loop()
{
	// Flush the serial input buffer
	Serial.flush();
	while (Serial.available() > 0) {
#if DEBUG
		Serial.print(F("!available() = "));
		Serial.println(Serial.available());
#endif
		Serial.read();
	}
	//
	char send_buffer_first[6];
	char send_buffer[6];
	const char *fmt = "S%4d";
	buffer_size++;
	if (buffer_size > MAX_BUFFER_SIZE) {
		buffer_size = MAX_BUFFER_SIZE;
	}
	snprintf(send_buffer_first, sizeof send_buffer_first, fmt, buffer_size);
	// Choice of threshold
	//threshold = buffer_size * 3 / 4 + 1;
	threshold = buffer_size;
	snprintf(send_buffer, sizeof send_buffer, fmt, threshold);
	//
	int c = -1;
	uint32_t count = 0;
	uint32_t n = BLOCK_SIZE;
	uint32_t current_threshold = threshold;
	Serial.print(F("!Buffer size: "));
	Serial.print(buffer_size);
	Serial.print(F(", threshold: "));
	Serial.println(threshold);
#if DEBUG
	Serial.print(F("!send_buffer_first="));
	Serial.println(send_buffer_first);
	Serial.print(F("!send_buffer="));
	Serial.println(send_buffer);
#endif
	//
	Serial.println(F("R"));
	Serial.println(send_buffer_first);
	while (n) {
		int a;
		while (n && (a = Serial.available()) > 0) {
#if DEBUG
			Serial.print(F("Dn="));
			Serial.println(n);
#endif
			c = Serial.read();
			// Process the data
			delayMicroseconds(50);
#if DEBUG
			Serial.print(F("Dc = "));
			Serial.print(c);
			Serial.print(F(", "));
			Serial.print(char(c));
			Serial.print(F(", a="));
			Serial.println(a);
#endif
			--n;
			++count;
			if (count == current_threshold) {
				Serial.println(send_buffer);
				current_threshold += threshold;
			}
#if DEBUG
			Serial.print(F("!count, threshold, available(): "));
			Serial.print(count);
			Serial.print(F(","));
			Serial.print(threshold);
			Serial.print(F(","));
			Serial.println(Serial.available());
#endif
		}
	}
	Serial.println(F("Q0,Ok"));
}

