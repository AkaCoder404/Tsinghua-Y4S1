src = 0x2402 + 0xF000 + 0x0001 + 0x0400 + 0x0000 + 0x0000 + 0x0000 + 0x0002
print(hex(src))
dst = 0x2402 + 0xF000 + 0x0001 + 0x0404 + 0x0166 + 0x0111 + 0x0004 + 0x0100
print(hex(dst))
print("src + dst", hex(src + dst))

payload_length = 0x12
nxt_header = 0x3A

psuedo_header_sum = src + dst + nxt_header + payload_length;
print("psuedo_header_sum", hex(psuedo_header_sum))

code = 0x81
echo = 0x00

echo_code = 0x8100
checksum = 0x7BBF
identifier = 0x4672
sequence = 0x2521
print(hex(echo_code + identifier + sequence))
data = 0x4274 + 0x0CF3 +0x4276 + 0x5A5E +  0x779B
print(hex(data))
icmp_sum = echo_code + identifier + sequence + data
print("icmp_sum", hex(icmp_sum))

summ = icmp_sum + psuedo_header_sum
while(summ&0xFFFF0000):
  summ = (summ>>16) + (summ&0xFFFF)

print("solve carry over", hex(summ))
summ = summ ^ 0xFFFF

print("ones compliment sum", hex(summ))