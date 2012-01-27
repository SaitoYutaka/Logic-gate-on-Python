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
   s = logical_xor(a, b)
   c = logical_and(a, b)
   return s, c

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
