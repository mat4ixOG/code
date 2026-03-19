from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        temp = '\n'
        for i in strs:
          temp = i + '\n'
          res = res +  ''.join(format(j , '08b') for j in temp.encode('utf-8'))
        return res
        

    def decode(self, s: str) -> List[str]:
        n = 8
        binary_chunks = [s[i:i + n] for i in range(0, len(s), n)]
        decoded_bytes = bytes([int(byte, 2) for byte in binary_chunks])
        decoded_str = decoded_bytes.decode('utf-8')
        result = (decoded_str.split('\n')[:-1])
        return result
       
    if __name__ == '__main__':
        sol = encode('' , ['deb' , 'is' , 'awesome'])
        decodedStr = decode('' , sol)
        print('encoded',sol)
        print('decoded',decodedStr)
        
