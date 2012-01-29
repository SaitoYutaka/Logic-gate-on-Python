def logical_or(a, b):
   """
     --+----*
        > OR >--
     --+----*
   """
   if(a == 0 and b == 0): return 0
   elif(a == 1 and b == 0): return 1
   elif(a == 0 and b == 1): return 1
   elif(a == 1 and b == 1): return 1
   else: return -1

def logical_xor(a, b):
   """
     --++----*
        >>XOR >--
     --++----*
   """
   if(a == 0 and b == 0): return 0
   elif(a == 1 and b == 0): return 1
   elif(a == 0 and b == 1): return 1
   elif(a == 1 and b == 1): return 0
   else: return -1

def logical_and(a, b):
   """
     --+----*
       | AND >--
     --+----*
   """
   if(a == 0 and b == 0): return 0
   elif(a == 1 and b == 0): return 0
   elif(a == 0 and b == 1): return 0
   elif(a == 1 and b == 1): return 1
   else: return -1

def logical_and_3input(a, b, c):
   """
     --+----*
     __| AND *---
       |     *
     --+----*
   """
   n = logical_and(a, b)
   s = logical_and(n, c)
   return s

def logical_not(a):
   """
     |*
   --+NOT>--
     |*
   """
   if(a == 1): return 0
   elif(a == 0): return 1
   else: return -1

def half_adder(a, b):
   """
 A ---+--++----*
      |   >>XOR >---- S
 B -+--)-++----*
    | |
    | +----+----*
    |      | AND >--- C
    +------+----*
   """
   s = logical_xor(a, b)
   c = logical_and(a, b)
   return c, s

def full_adder(a, b, c):
   """
 A ---+--++----* 'o1'
      |   >>XOR >------+---++----*
 B -+--)-++----*       |    >>XOR >------------ S
    | |            +----)--++----*
 C --)-)-----------+   |
    | |            |   +--+----* 'o2'
    | |            |      | AND >--+
    | |            +------+----*   +--+----*
    | |                                > OR >-- C out
    | +-------------------+----*   +--+----*
    |                     | AND >--+
    +---------------------+----* 'o3'
   """
   o1 = logical_xor(a, b)
   o2 = logical_and(o1, c)
   o3 = logical_and(a, b)
   s  = logical_xor(o1, c)
   c_out = logical_or(o2, o3)
   return c_out, s

def four_bit_adder(a3, b3, a2, b2, a1, b1, a0, b0):
   """
     a3 b3      a2 b2      a1 b1      a0 b0 
      |  |       |  |       |  |       |  |      
     ++--+-+    ++--+-+    ++--+-+    ++--+-+  
  c4 |1-bit| c3 |1-bit| c2 |1-bit| c1 |1-bit|  
  <--+Full +<---+Full +<---+Full +<---+Half |
     |Adder|    |Adder|    |Adder|    |Adder|  
     +-+---+    +-+---+    +-+---+    +-+---+  
       |          |          |          |      
      s3         s2         s1         s0 
   """

   c1, s0 = half_adder(a0, b0)
   c2, s1 = full_adder(a1, b1, c1)
   c3, s2 = full_adder(a2, b2, c2)
   c4, s3 = full_adder(a3, b3, c3)

   return c4, s3, s2, s1 ,s0

def make_bit_array(n):
   b0 = b1 = b2 = b3 = 0
   if((n & 0x8) == 0x8): b3 = 1 
   if((n & 0x4) == 0x4): b2 = 1
   if((n & 0x2) == 0x2): b1 = 1 
   if((n & 0x1) == 0x1): b0 = 1 
   return b0, b1, b2, b3

def make_num(b0, b1, b2, b3):
   num = 0
   if(b3 == 1): num |= 0x8
   if(b2 == 1): num |= 0x4
   if(b1 == 1): num |= 0x2
   if(b0 == 1): num |= 0x1
   return num

def plus(n1, n2):
   if((0x0f < n1 ) or (0x0f < n2)):
      print('error')
   else:
      a0, a1, a2, a3 = make_bit_array(n1)
      b0, b1, b2, b3 = make_bit_array(n2)
      c4, s3, s2, s1 ,s0 = four_bit_adder(a3, b3, a2, b2, a1, b1, a0, b0)
      
      ret = make_num(s0, s1, s2, s3)
      if(c4 == 1): ret |= 0x10
      return ret

def two_to_one_mux(a, b, s):
   """
         A    B
         |    |   
      ---+----+---
      *          *
       *        *--- S
        *------*
           |
           Z
   """
   if((s == 0) and (a == 1) and (b == 1)): return 1
   if((s == 0) and (a == 1) and (b == 0)): return 1
   if((s == 0) and (a == 0) and (b == 1)): return 0
   if((s == 0) and (a == 0) and (b == 0)): return 0
   if((s == 1) and (a == 1) and (b == 1)): return 1
   if((s == 1) and (a == 1) and (b == 0)): return 0
   if((s == 1) and (a == 0) and (b == 1)): return 1
   if((s == 1) and (a == 0) and (b == 0)): return 0
   return -1

def four_to_one_mux():
   pass
   
