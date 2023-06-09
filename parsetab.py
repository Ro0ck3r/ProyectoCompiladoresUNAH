
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMRESleftPOTMULTDIVrightUMENOSleftAPARENTCPARENTleftACORCCORACOR APARENT CCOR CPARENT DECIMAL DIV FINAL MULT NUMERO OPERAR POT RES SUMinstrucciones    : instruccion instrucciones\n                        | instruccion instruccion : OPERAR ACOR expresion CCOR FINALinstruccion : expresionexpresion : expresion SUM expresion\n                  | expresion RES expresion\n                  | expresion MULT expresion\n                  | expresion DIV expresion\n                  | expresion POT expresionexpresion : RES expresion %prec UMENOSexpresion : APARENT expresion CPARENTexpresion    : NUMERO\n                    | DECIMAL'
    
_lr_action_items = {'OPERAR':([0,2,4,7,8,16,19,20,21,22,23,24,26,],[3,3,-4,-12,-13,-10,-5,-6,-7,-8,-9,-11,-3,]),'RES':([0,2,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,],[5,5,12,5,5,-12,-13,5,5,5,5,5,5,-10,12,12,-5,-6,-7,-8,-9,-11,-3,]),'APARENT':([0,2,4,5,6,7,8,10,11,12,13,14,15,16,19,20,21,22,23,24,26,],[6,6,-4,6,6,-12,-13,6,6,6,6,6,6,-10,-5,-6,-7,-8,-9,-11,-3,]),'NUMERO':([0,2,4,5,6,7,8,10,11,12,13,14,15,16,19,20,21,22,23,24,26,],[7,7,-4,7,7,-12,-13,7,7,7,7,7,7,-10,-5,-6,-7,-8,-9,-11,-3,]),'DECIMAL':([0,2,4,5,6,7,8,10,11,12,13,14,15,16,19,20,21,22,23,24,26,],[8,8,-4,8,8,-12,-13,8,8,8,8,8,8,-10,-5,-6,-7,-8,-9,-11,-3,]),'$end':([1,2,4,7,8,9,16,19,20,21,22,23,24,26,],[0,-2,-4,-12,-13,-1,-10,-5,-6,-7,-8,-9,-11,-3,]),'ACOR':([3,],[10,]),'SUM':([4,7,8,16,17,18,19,20,21,22,23,24,],[11,-12,-13,-10,11,11,-5,-6,-7,-8,-9,-11,]),'MULT':([4,7,8,16,17,18,19,20,21,22,23,24,],[13,-12,-13,-10,13,13,13,13,-7,-8,-9,-11,]),'DIV':([4,7,8,16,17,18,19,20,21,22,23,24,],[14,-12,-13,-10,14,14,14,14,-7,-8,-9,-11,]),'POT':([4,7,8,16,17,18,19,20,21,22,23,24,],[15,-12,-13,-10,15,15,15,15,-7,-8,-9,-11,]),'CPARENT':([7,8,16,17,19,20,21,22,23,24,],[-12,-13,-10,24,-5,-6,-7,-8,-9,-11,]),'CCOR':([7,8,16,18,19,20,21,22,23,24,],[-12,-13,-10,25,-5,-6,-7,-8,-9,-11,]),'FINAL':([25,],[26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,2,],[1,9,]),'instruccion':([0,2,],[2,2,]),'expresion':([0,2,5,6,10,11,12,13,14,15,],[4,4,16,17,18,19,20,21,22,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones_lista','AnalizadorSintactico.py',15),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','AnalizadorSintactico.py',16),
  ('instruccion -> OPERAR ACOR expresion CCOR FINAL','instruccion',5,'p_instrucciones_operar','AnalizadorSintactico.py',20),
  ('instruccion -> expresion','instruccion',1,'p_instrucciones_expr','AnalizadorSintactico.py',27),
  ('expresion -> expresion SUM expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',31),
  ('expresion -> expresion RES expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',32),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',33),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',34),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',35),
  ('expresion -> RES expresion','expresion',2,'p_expresion_unaria','AnalizadorSintactico.py',50),
  ('expresion -> APARENT expresion CPARENT','expresion',3,'p_expresion_agrupacion','AnalizadorSintactico.py',54),
  ('expresion -> NUMERO','expresion',1,'p_expresion_number','AnalizadorSintactico.py',59),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_number','AnalizadorSintactico.py',60),
]
