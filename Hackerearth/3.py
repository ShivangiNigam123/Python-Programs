#Jadoo and DNA Transcription
Dstring = input()
Rstring = ""
Flag='T'
for x in Dstring :
  if x not in ['G', 'C','A','T'] :
       print('Invalid Input')
       Flag='F'
       break
  else :
      if x =='G':
          Rstring +='C'
      elif x =='C':
          Rstring +='G'
      elif x =='T' :
          Rstring +='A'
      elif x =='A' :
          Rstring +='U'
if Flag=='T' :
  print (Rstring)

