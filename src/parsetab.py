
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL AND CARDINALITY CLASS EXACTLY IDENT_LPAREN INDIVIDUAL KEYWORD LPAREN MAX MIN NAMESPACE NOT NUMERAL OR PROPERTY RPAREN SOME SPECIAL_SYMBOL THAT TWOPOINTS TYPE VALUEprimitive_class : KEYWORD TWOPOINTS CLASS sub_class_of disjoint_classes individuals\n                       | empty\n    sub_class_of : KEYWORD TWOPOINTS sub_class_expression sub_class_of_optional\n                    | empty\n    sub_class_of_optional : sub_class_expression sub_class_of\n                              | disjoint_classes\n                              | empty\n    \n        sub_class_expression : PROPERTY KEYWORD CLASS sub_class_expression\n                             | SPECIAL_SYMBOL PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE sub_class_expression\n                             | empty\n    \n        disjoint_classes : KEYWORD TWOPOINTS CLASS disjoint_classes\n                         | SPECIAL_SYMBOL CLASS disjoint_classes\n                         | empty\n    \n        individuals : KEYWORD TWOPOINTS INDIVIDUAL individuals\n                    | SPECIAL_SYMBOL INDIVIDUAL\n                    | empty\n    empty :'
    
_lr_action_items = {'KEYWORD':([0,5,7,8,9,11,13,14,15,17,23,24,25,26,27,30,31,34,35,36,38,39,40,44,45,],[2,6,10,-4,-17,19,-13,10,29,-10,10,6,-3,-6,-7,37,10,-12,-5,-17,-11,19,-8,-17,-9,]),'$end':([0,1,3,5,7,8,9,11,13,14,17,20,22,23,24,25,26,27,31,33,34,35,36,38,39,40,42,44,45,],[-17,0,-2,-17,-17,-4,-17,-17,-13,-17,-10,-1,-16,-17,-17,-3,-6,-7,-17,-15,-12,-5,-17,-11,-17,-8,-14,-17,-9,]),'TWOPOINTS':([2,6,10,19,41,],[4,9,18,32,43,]),'CLASS':([4,12,18,28,29,],[5,23,31,23,36,]),'SPECIAL_SYMBOL':([5,7,8,9,11,13,14,17,23,24,25,26,27,31,34,35,36,38,39,40,44,45,],[-17,12,-4,16,21,-13,28,-10,12,-17,-3,-6,-7,12,-12,-5,16,-11,21,-8,16,-9,]),'PROPERTY':([9,14,16,17,28,36,40,44,45,],[15,15,30,-10,30,15,-8,15,-9,]),'INDIVIDUAL':([21,32,],[33,39,]),'NAMESPACE':([37,],[41,]),'TYPE':([43,],[44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'primitive_class':([0,],[1,]),'empty':([0,5,7,9,11,14,23,24,31,36,39,44,],[3,8,13,17,22,27,13,8,13,17,22,17,]),'sub_class_of':([5,24,],[7,35,]),'disjoint_classes':([7,14,23,31,],[11,26,34,38,]),'sub_class_expression':([9,14,36,44,],[14,24,40,45,]),'individuals':([11,39,],[20,42,]),'sub_class_of_optional':([14,],[25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> primitive_class","S'",1,None,None,None),
  ('primitive_class -> KEYWORD TWOPOINTS CLASS sub_class_of disjoint_classes individuals','primitive_class',6,'p_primitive_class','osa.py',28),
  ('primitive_class -> empty','primitive_class',1,'p_primitive_class','osa.py',29),
  ('sub_class_of -> KEYWORD TWOPOINTS sub_class_expression sub_class_of_optional','sub_class_of',4,'p_sub_class_of','osa.py',39),
  ('sub_class_of -> empty','sub_class_of',1,'p_sub_class_of','osa.py',40),
  ('sub_class_of_optional -> sub_class_expression sub_class_of','sub_class_of_optional',2,'p_sub_class_of_optional','osa.py',44),
  ('sub_class_of_optional -> disjoint_classes','sub_class_of_optional',1,'p_sub_class_of_optional','osa.py',45),
  ('sub_class_of_optional -> empty','sub_class_of_optional',1,'p_sub_class_of_optional','osa.py',46),
  ('sub_class_expression -> PROPERTY KEYWORD CLASS sub_class_expression','sub_class_expression',4,'p_sub_class_expression','osa.py',53),
  ('sub_class_expression -> SPECIAL_SYMBOL PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE sub_class_expression','sub_class_expression',7,'p_sub_class_expression','osa.py',54),
  ('sub_class_expression -> empty','sub_class_expression',1,'p_sub_class_expression','osa.py',55),
  ('disjoint_classes -> KEYWORD TWOPOINTS CLASS disjoint_classes','disjoint_classes',4,'p_disjoint_classes','osa.py',60),
  ('disjoint_classes -> SPECIAL_SYMBOL CLASS disjoint_classes','disjoint_classes',3,'p_disjoint_classes','osa.py',61),
  ('disjoint_classes -> empty','disjoint_classes',1,'p_disjoint_classes','osa.py',62),
  ('individuals -> KEYWORD TWOPOINTS INDIVIDUAL individuals','individuals',4,'p_individuals','osa.py',67),
  ('individuals -> SPECIAL_SYMBOL INDIVIDUAL','individuals',2,'p_individuals','osa.py',68),
  ('individuals -> empty','individuals',1,'p_individuals','osa.py',69),
  ('empty -> <empty>','empty',0,'p_empty','osa.py',73),
]
