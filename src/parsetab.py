
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL AND CARDINALITY CLASS EXACTLY IDENT_LPAREN INDIVIDUAL INSTANCE KEYWORD KEYWORD_CLASS KEYWORD_DISJOINT KEYWORD_EQUIVALENTTO KEYWORD_INDIVIDUALS KEYWORD_SUBCLASSOF LCOLCH LKEY LPAREN MAX MIN NAMESPACE NEWLINE NOT NUMERAL OR PROPERTY RCOLCH RKEY RPAREN SOME SPECIAL_SYMBOL THAT TWOPOINTS TYPE VALUE\n\n    S : primitive_class\n      | defined_class\n      | closure_class\n      | nested_class\n      | covered_class\n      | enumerated_class\n      | other_class\n      | empty\n\n    primitive_class : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of disjoint_classes individuals primitive_class\n                    | empty\n\n    other_class     : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of individuals other_class\n                    | empty\n\n    defined_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals defined_class\n                  | empty\n\n    nested_class  : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to\n                  | empty\n\n    covered_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals\n                  | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to\n\n    enumerated_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals\n                     | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to\n\n    closure_class : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of\n                  | empty\n\n    sub_class_of : KEYWORD_SUBCLASSOF TWOPOINTS sub_class_expression sub_class_of_optional\n                 | KEYWORD_SUBCLASSOF TWOPOINTS CLASS KEYWORD sub_class_of\n                 | KEYWORD_SUBCLASSOF TWOPOINTS CLASS SPECIAL_SYMBOL sub_class_of\n                 | KEYWORD_SUBCLASSOF TWOPOINTS NAMESPACE KEYWORD LPAREN property_expression sub_class_of\n                 | KEYWORD_SUBCLASSOF CLASS SPECIAL_SYMBOL sub_class_of\n                 | PROPERTY KEYWORD CLASS SPECIAL_SYMBOL sub_class_of\n                 | PROPERTY KEYWORD LPAREN CLASS RPAREN sub_class_of\n                 | PROPERTY KEYWORD LPAREN equivalent_to_covered_expression RPAREN sub_class_of\n                 | empty\n\n    sub_class_expression : PROPERTY KEYWORD CLASS sub_class_expression\n                         | SPECIAL_SYMBOL PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE sub_class_expression\n                         | empty\n\n\n    sub_class_of_optional : sub_class_expression sub_class_of\n                          | disjoint_classes\n                          | empty\n\n    equivalent_to : KEYWORD_EQUIVALENTTO TWOPOINTS equivalent_to_expression\n                  | empty\n\n\n\n    equivalent_to_expression : CLASS KEYWORD LPAREN PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE LCOLCH SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL RCOLCH RPAREN\n                             | CLASS KEYWORD LPAREN PROPERTY KEYWORD CLASS RPAREN equivalent_to_expression\n                             | CLASS KEYWORD LPAREN PROPERTY KEYWORD LPAREN property_expression equivalent_to_expression\n                             | KEYWORD LPAREN PROPERTY KEYWORD LPAREN property_expression equivalent_to_expression\n                             | KEYWORD LPAREN PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE RPAREN equivalent_to_expression\n                             | SPECIAL_SYMBOL CLASS equivalent_to_expression\n                             | SPECIAL_SYMBOL CLASS SPECIAL_SYMBOL equivalent_to_expression\n                             | equivalent_to_enumerated_expression\n                             | equivalent_to_nested_expression\n                             | equivalent_to_covered_expression\n                             | empty\n\n    equivalent_to_enumerated_expression  : LKEY INSTANCE SPECIAL_SYMBOL\n                                        | INSTANCE SPECIAL_SYMBOL\n                                        | INSTANCE RKEY\n                                        | empty\n\n    equivalent_to_nested_expression : CLASS KEYWORD equivalent_to_nested_expression\n                                    | KEYWORD LPAREN PROPERTY KEYWORD equivalent_to_nested_expression\n                                    | LPAREN PROPERTY KEYWORD CLASS RPAREN equivalent_to_nested_expression\n                                    |\n\n    individuals : KEYWORD_INDIVIDUALS TWOPOINTS INDIVIDUAL individuals\n                | SPECIAL_SYMBOL INDIVIDUAL individuals\n                | empty\n\n    property_expression  : PROPERTY KEYWORD CLASS SPECIAL_SYMBOL property_expression\n                         | PROPERTY KEYWORD NUMERAL NAMESPACE TWOPOINTS TYPE property_expression\n                         | PROPERTY KEYWORD LPAREN property_expression\n                         | PROPERTY KEYWORD property_expression_closure\n                         | PROPERTY KEYWORD CLASS RPAREN property_expression\n                         | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL\n                         | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL\n                         | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE RPAREN\n                         | RPAREN property_expression\n                         | empty\n\n    equivalent_to_covered_expression : CLASS KEYWORD equivalent_to_covered_expression\n                                     | CLASS equivalent_to_covered_expression\n                                     | KEYWORD CLASS\n                                     | empty\n\n    disjoint_classes : KEYWORD_DISJOINT TWOPOINTS CLASS disjoint_classes\n                     | SPECIAL_SYMBOL CLASS disjoint_classes\n                     | empty\n\n    property_expression_closure : LPAREN CLASS property_expression_closure\n                                | KEYWORD CLASS property_expression_closure\n                                | KEYWORD CLASS RPAREN property_expression\n                                | empty\n\n    nested_descriptions_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals\n                              | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to\n\n\n    empty :'
    
_lr_action_items = {'KEYWORD_CLASS':([0,12,13,14,17,19,20,23,25,27,28,31,32,37,38,43,48,49,52,53,57,58,59,60,67,69,70,71,72,74,75,76,77,79,80,84,85,86,90,91,92,93,95,97,99,100,102,103,104,105,106,107,108,110,111,112,113,114,115,116,119,120,123,124,125,126,127,128,129,131,133,134,135,136,137,138,139,142,144,145,146,147,149,150,151,155,157,159,160,161,162,163,164,169,170,171,172,174,177,179,180,181,183,184,185,186,189,190,191,192,194,195,197,200,201,203,204,207,208,209,210,213,214,215,216,217,219,221,222,224,226,230,233,235,237,240,],[10,-85,-85,-85,-31,-85,33,-61,40,-61,-85,-58,63,-85,-85,-85,-34,-85,-38,-85,-47,-48,-49,-50,-85,-77,-78,-60,-85,-85,-23,-36,-34,-85,-85,-27,-31,-85,-75,-85,-58,-73,-74,-58,-52,-53,-85,-76,-59,-85,-35,-24,-25,-85,-85,-28,-85,-85,-85,-74,-55,-72,-58,-45,-51,-85,-85,-85,-39,-85,-85,-71,-32,-74,-29,-30,-58,-58,-58,-46,-85,40,-26,-85,-70,-85,-56,-58,-85,-58,-49,-50,-85,-85,-65,-82,-58,-85,-58,-58,-57,-58,-33,-85,-85,-85,-64,-85,-58,-58,-85,-43,-74,-80,-85,-62,-66,-79,-41,-48,-42,-58,-58,-58,-81,-85,-69,-58,-44,-85,-63,-58,-68,-42,-67,-40,]),'$end':([0,1,2,3,4,5,6,7,8,9,12,13,14,17,19,20,23,25,27,28,31,32,34,35,37,38,41,42,43,48,49,52,53,57,58,59,60,64,65,67,69,70,71,72,74,75,76,77,79,80,84,85,86,90,91,92,93,95,97,99,100,102,103,104,105,106,107,108,110,111,112,113,114,115,116,119,120,123,124,125,126,127,128,129,131,133,134,135,136,137,138,139,142,144,145,146,147,149,150,151,155,157,159,160,161,162,163,164,169,170,171,172,174,177,179,180,181,183,184,185,186,189,190,191,192,194,195,197,200,201,203,204,207,208,209,210,213,214,215,216,217,219,221,222,224,226,230,233,235,237,240,],[-85,0,-1,-2,-3,-4,-5,-6,-7,-8,-85,-21,-15,-31,-85,-85,-61,-17,-61,-85,-58,-85,-11,-12,-85,-85,-13,-14,-85,-34,-85,-38,-85,-47,-48,-49,-50,-9,-10,-85,-77,-78,-60,-85,-85,-23,-36,-34,-85,-85,-27,-31,-85,-75,-85,-58,-73,-74,-58,-52,-53,-85,-76,-59,-85,-35,-24,-25,-85,-85,-28,-85,-85,-85,-74,-55,-72,-58,-45,-51,-85,-85,-85,-39,-85,-85,-71,-32,-74,-29,-30,-58,-58,-58,-46,-85,-85,-26,-85,-70,-85,-56,-58,-85,-58,-49,-50,-85,-85,-65,-82,-58,-85,-58,-58,-57,-58,-33,-85,-85,-85,-64,-85,-58,-58,-85,-43,-74,-80,-85,-62,-66,-79,-41,-48,-42,-58,-58,-58,-81,-85,-69,-58,-44,-85,-63,-58,-68,-42,-67,-40,]),'TWOPOINTS':([10,15,18,21,24,33,40,63,130,156,168,175,187,225,],[11,28,31,36,39,66,73,101,148,178,188,193,205,231,]),'CLASS':([11,15,22,28,30,31,36,51,53,54,56,66,68,73,78,83,87,88,91,92,97,101,113,116,117,122,123,133,134,136,139,142,144,150,151,153,155,159,160,161,165,169,170,171,172,174,177,179,181,184,185,186,189,190,191,192,194,197,198,200,201,202,203,204,207,213,214,215,216,217,219,221,224,226,230,233,237,],[12,29,37,44,50,53,67,88,91,95,97,102,37,105,37,111,95,91,91,116,53,126,136,91,95,143,144,-85,-71,91,116,158,160,166,-70,173,-85,158,91,116,184,190,-65,-82,158,-85,53,158,197,-85,-85,-85,-64,-85,53,53,212,91,95,-80,-85,190,-62,-66,-79,53,197,223,-81,-85,-69,158,-85,-63,53,-68,-67,]),'KEYWORD_SUBCLASSOF':([12,28,43,48,49,74,77,79,80,86,102,110,111,114,115,126,131,133,134,135,150,151,164,169,170,171,183,184,185,186,189,190,200,201,203,204,207,216,217,219,226,233,237,],[15,-85,-85,-34,15,15,-34,15,15,15,15,-85,-85,15,15,15,15,-85,-71,-32,-85,-70,-85,-85,-65,-82,-33,-85,-85,-85,-64,-85,-80,-85,-62,-66,-79,-81,-85,-69,-63,-68,-67,]),'PROPERTY':([12,28,43,45,48,49,55,74,77,78,79,80,86,94,102,110,111,114,115,118,126,131,133,134,135,140,150,151,155,164,169,170,171,174,182,183,184,185,186,189,190,200,201,203,204,207,216,217,219,221,224,226,233,237,],[16,47,47,81,-34,16,96,16,-34,81,16,16,16,121,16,132,47,16,16,141,16,16,132,-71,-32,152,-85,-70,176,47,132,-65,-82,132,199,-33,-85,132,132,-64,-85,-80,132,-62,-66,-79,-81,132,-69,132,176,-63,-68,-67,]),'KEYWORD_EQUIVALENTTO':([12,105,],[18,18,]),'KEYWORD_DISJOINT':([12,13,17,28,37,43,48,49,67,69,70,74,75,76,77,79,80,84,85,86,103,106,107,108,110,111,112,114,115,126,131,133,134,135,137,138,146,149,150,151,164,169,170,171,183,184,185,186,189,190,200,201,203,204,207,216,217,219,226,233,237,],[-85,21,-31,-85,21,21,-34,-85,21,-77,-78,-85,-23,-36,-34,-85,-85,-27,-31,-85,-76,-35,-24,-25,-85,-85,-28,-85,-85,-85,-85,-85,-71,-32,-29,-30,21,-26,-85,-70,-85,-85,-65,-82,-33,-85,-85,-85,-64,-85,-80,-85,-62,-66,-79,-81,-85,-69,-63,-68,-67,]),'SPECIAL_SYMBOL':([12,13,14,17,19,23,28,29,31,37,38,43,44,48,49,50,52,53,57,58,59,60,62,67,69,70,72,74,75,76,77,79,80,84,85,86,90,91,92,93,95,97,98,99,100,102,103,105,106,107,108,110,111,112,113,114,115,116,119,120,123,124,125,126,127,128,129,131,133,134,135,136,137,138,139,142,144,145,146,149,150,151,155,157,159,160,161,162,163,164,166,169,170,171,172,174,177,179,180,181,183,184,185,186,189,190,191,192,194,195,197,200,201,203,204,206,207,208,209,210,212,213,214,215,216,217,218,219,220,221,222,224,226,228,229,230,232,233,235,237,240,],[-85,22,26,-31,26,-78,45,49,56,68,26,78,80,-34,-85,86,-38,-85,-47,-48,-49,-50,99,68,-77,-78,26,-85,-23,-36,-34,-85,-85,-27,-31,-85,-75,-85,-58,-73,-74,123,125,-52,-53,-85,-76,-85,-35,-24,-25,-85,45,-28,-85,-85,-85,-74,-55,-72,56,-45,-51,-85,26,26,-39,-85,-85,-71,-32,-74,-29,-30,-58,-58,123,-46,68,-26,-85,-70,-85,-56,-58,-85,-58,-49,-50,45,185,-85,-65,-82,-58,-85,56,-58,-57,-58,-33,-85,-85,-85,-64,-85,56,56,-85,-43,-74,-80,-85,-62,-66,218,-79,-41,-48,-42,185,56,-58,-58,-81,-85,227,-69,229,-58,-44,-85,-63,233,234,56,237,-68,-42,-67,-40,]),'KEYWORD_INDIVIDUALS':([12,13,14,17,19,23,28,31,37,38,43,48,49,52,53,57,58,59,60,67,69,70,72,74,75,76,77,79,80,84,85,86,90,91,92,93,95,97,99,100,102,103,105,106,107,108,110,111,112,113,114,115,116,119,120,123,124,125,126,127,128,129,131,133,134,135,136,137,138,139,142,144,145,146,149,150,151,155,157,159,160,161,162,163,164,169,170,171,172,174,177,179,180,181,183,184,185,186,189,190,191,192,194,195,197,200,201,203,204,207,208,209,210,213,214,215,216,217,219,221,222,224,226,230,233,235,237,240,],[-85,24,24,-31,24,-78,-85,-58,-85,24,-85,-34,-85,-38,-85,-47,-48,-49,-50,-85,-77,-78,24,-85,-23,-36,-34,-85,-85,-27,-31,-85,-75,-85,-58,-73,-74,-58,-52,-53,-85,-76,-85,-35,-24,-25,-85,-85,-28,-85,-85,-85,-74,-55,-72,-58,-45,-51,-85,24,24,-39,-85,-85,-71,-32,-74,-29,-30,-58,-58,-58,-46,-85,-26,-85,-70,-85,-56,-58,-85,-58,-49,-50,-85,-85,-65,-82,-58,-85,-58,-58,-57,-58,-33,-85,-85,-85,-64,-85,-58,-58,-85,-43,-74,-80,-85,-62,-66,-79,-41,-48,-42,-58,-58,-58,-81,-85,-69,-58,-44,-85,-63,-58,-68,-42,-67,-40,]),'KEYWORD':([16,31,44,46,47,51,53,81,88,91,92,96,97,113,116,121,123,132,133,134,136,139,141,142,144,150,151,152,155,158,159,160,161,169,170,171,172,174,176,177,179,181,184,185,186,189,190,191,192,194,197,199,200,201,203,204,207,213,214,215,216,217,219,221,223,224,226,230,233,237,],[30,54,79,82,83,87,92,109,113,113,117,122,54,87,139,142,54,150,-85,-71,113,117,153,154,161,165,-70,172,-85,179,154,181,117,-85,-65,-82,154,-85,194,54,154,198,165,-85,-85,-64,165,54,54,165,214,215,-80,-85,-62,-66,-79,54,198,154,-81,-85,-69,154,179,-85,-63,54,-68,-67,]),'INDIVIDUAL':([22,26,39,],[38,38,72,]),'NAMESPACE':([28,109,142,150,153,167,194,215,],[46,130,156,168,175,187,168,225,]),'LPAREN':([30,31,54,82,92,97,117,123,133,134,139,142,144,150,151,153,154,155,159,161,169,170,171,172,174,177,179,181,184,185,186,189,190,191,192,194,198,200,201,203,204,207,213,214,215,216,217,219,221,224,226,230,233,237,],[51,55,94,110,118,55,140,55,-85,-71,55,155,55,169,-70,174,140,-85,55,182,-85,-65,-82,55,-85,55,55,118,202,-85,-85,-64,202,55,55,169,140,-80,-85,-62,-66,-79,55,55,224,-81,-85,-69,55,-85,-63,55,-68,-67,]),'LKEY':([31,97,123,133,134,144,150,151,155,169,170,171,174,177,184,185,186,189,190,191,192,194,200,201,203,204,207,213,216,217,219,221,224,226,230,233,237,],[61,61,61,-85,-71,61,-85,-70,-85,-85,-65,-82,-85,61,-85,-85,-85,-64,-85,61,61,-85,-80,-85,-62,-66,-79,61,-81,-85,-69,-85,-85,-63,61,-68,-67,]),'INSTANCE':([31,61,97,123,133,134,144,150,151,155,169,170,171,174,177,184,185,186,189,190,191,192,194,200,201,203,204,207,213,216,217,219,221,224,226,230,233,237,],[62,98,62,62,-85,-71,62,-85,-70,-85,-85,-65,-82,-85,62,-85,-85,-85,-64,-85,62,62,-85,-80,-85,-62,-66,-79,62,-81,-85,-69,-85,-85,-63,62,-68,-67,]),'RPAREN':([51,88,89,90,91,93,95,110,113,120,133,136,143,155,166,169,173,174,184,185,186,196,201,206,212,217,221,223,224,236,239,],[-85,114,115,-75,-85,-73,-74,133,-85,-72,133,-74,159,133,186,133,191,133,201,133,133,213,133,219,221,133,133,191,133,213,240,]),'RKEY':([62,],[100,]),'TYPE':([148,178,188,193,205,231,],[164,196,206,211,217,236,]),'NUMERAL':([150,194,218,227,234,],[167,167,228,232,238,]),'LCOLCH':([211,236,],[220,220,]),'RCOLCH':([238,],[239,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'primitive_class':([0,32,],[2,64,]),'defined_class':([0,25,147,],[3,41,41,]),'closure_class':([0,],[4,]),'nested_class':([0,],[5,]),'covered_class':([0,],[6,]),'enumerated_class':([0,],[7,]),'other_class':([0,20,],[8,34,]),'empty':([0,12,13,14,19,20,25,28,31,32,37,38,43,49,51,53,67,72,74,79,80,86,88,91,92,97,102,105,110,111,113,114,115,116,123,126,127,128,131,133,136,139,144,146,147,150,155,160,161,164,169,174,177,181,184,185,186,190,191,192,194,197,201,213,214,217,221,224,230,],[9,17,23,27,27,35,42,48,60,65,70,27,77,85,90,90,70,27,85,85,85,85,90,90,90,60,85,129,134,48,90,85,85,90,60,85,27,27,85,134,90,90,163,70,42,171,134,90,90,48,134,134,60,90,171,134,134,171,60,60,171,90,134,60,90,134,134,134,60,]),'sub_class_of':([12,49,74,79,80,86,102,114,115,126,131,],[13,84,106,107,108,112,127,137,138,146,149,]),'equivalent_to':([12,105,],[14,128,]),'disjoint_classes':([13,37,43,67,146,],[19,69,76,103,19,]),'individuals':([13,14,19,38,72,127,128,],[20,25,32,71,104,20,147,]),'sub_class_expression':([28,43,111,164,],[43,74,135,183,]),'equivalent_to_expression':([31,97,123,144,177,191,192,213,230,],[52,124,145,124,195,208,210,222,235,]),'equivalent_to_enumerated_expression':([31,97,123,144,177,191,192,213,230,],[57,57,57,57,57,57,57,57,57,]),'equivalent_to_nested_expression':([31,92,97,123,139,142,144,159,161,172,177,179,181,191,192,213,214,215,221,230,],[58,119,58,58,119,157,58,180,119,157,58,119,119,209,58,58,119,157,180,58,]),'equivalent_to_covered_expression':([31,51,53,88,91,92,97,113,116,123,136,139,144,160,161,177,181,191,192,197,213,214,230,],[59,89,93,93,93,120,59,120,93,59,93,120,162,93,120,59,120,59,59,93,59,120,59,]),'sub_class_of_optional':([43,],[75,]),'property_expression':([110,133,155,169,174,185,186,201,217,221,224,],[131,151,177,189,192,203,204,216,226,204,230,]),'property_expression_closure':([150,184,190,194,],[170,200,207,170,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> primitive_class','S',1,'p_start','osa.py',24),
  ('S -> defined_class','S',1,'p_start','osa.py',25),
  ('S -> closure_class','S',1,'p_start','osa.py',26),
  ('S -> nested_class','S',1,'p_start','osa.py',27),
  ('S -> covered_class','S',1,'p_start','osa.py',28),
  ('S -> enumerated_class','S',1,'p_start','osa.py',29),
  ('S -> other_class','S',1,'p_start','osa.py',30),
  ('S -> empty','S',1,'p_start','osa.py',31),
  ('primitive_class -> KEYWORD_CLASS TWOPOINTS CLASS sub_class_of disjoint_classes individuals primitive_class','primitive_class',7,'p_start','osa.py',33),
  ('primitive_class -> empty','primitive_class',1,'p_start','osa.py',34),
  ('other_class -> KEYWORD_CLASS TWOPOINTS CLASS sub_class_of individuals other_class','other_class',6,'p_start','osa.py',36),
  ('other_class -> empty','other_class',1,'p_start','osa.py',37),
  ('defined_class -> KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals defined_class','defined_class',6,'p_start','osa.py',39),
  ('defined_class -> empty','defined_class',1,'p_start','osa.py',40),
  ('nested_class -> KEYWORD_CLASS TWOPOINTS CLASS equivalent_to','nested_class',4,'p_start','osa.py',42),
  ('nested_class -> empty','nested_class',1,'p_start','osa.py',43),
  ('covered_class -> KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals','covered_class',5,'p_start','osa.py',45),
  ('covered_class -> KEYWORD_CLASS TWOPOINTS CLASS equivalent_to','covered_class',4,'p_start','osa.py',46),
  ('enumerated_class -> KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals','enumerated_class',5,'p_start','osa.py',48),
  ('enumerated_class -> KEYWORD_CLASS TWOPOINTS CLASS equivalent_to','enumerated_class',4,'p_start','osa.py',49),
  ('closure_class -> KEYWORD_CLASS TWOPOINTS CLASS sub_class_of','closure_class',4,'p_start','osa.py',51),
  ('closure_class -> empty','closure_class',1,'p_start','osa.py',52),
  ('sub_class_of -> KEYWORD_SUBCLASSOF TWOPOINTS sub_class_expression sub_class_of_optional','sub_class_of',4,'p_start','osa.py',54),
  ('sub_class_of -> KEYWORD_SUBCLASSOF TWOPOINTS CLASS KEYWORD sub_class_of','sub_class_of',5,'p_start','osa.py',55),
  ('sub_class_of -> KEYWORD_SUBCLASSOF TWOPOINTS CLASS SPECIAL_SYMBOL sub_class_of','sub_class_of',5,'p_start','osa.py',56),
  ('sub_class_of -> KEYWORD_SUBCLASSOF TWOPOINTS NAMESPACE KEYWORD LPAREN property_expression sub_class_of','sub_class_of',7,'p_start','osa.py',57),
  ('sub_class_of -> KEYWORD_SUBCLASSOF CLASS SPECIAL_SYMBOL sub_class_of','sub_class_of',4,'p_start','osa.py',58),
  ('sub_class_of -> PROPERTY KEYWORD CLASS SPECIAL_SYMBOL sub_class_of','sub_class_of',5,'p_start','osa.py',59),
  ('sub_class_of -> PROPERTY KEYWORD LPAREN CLASS RPAREN sub_class_of','sub_class_of',6,'p_start','osa.py',60),
  ('sub_class_of -> PROPERTY KEYWORD LPAREN equivalent_to_covered_expression RPAREN sub_class_of','sub_class_of',6,'p_start','osa.py',61),
  ('sub_class_of -> empty','sub_class_of',1,'p_start','osa.py',62),
  ('sub_class_expression -> PROPERTY KEYWORD CLASS sub_class_expression','sub_class_expression',4,'p_start','osa.py',64),
  ('sub_class_expression -> SPECIAL_SYMBOL PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE sub_class_expression','sub_class_expression',7,'p_start','osa.py',65),
  ('sub_class_expression -> empty','sub_class_expression',1,'p_start','osa.py',66),
  ('sub_class_of_optional -> sub_class_expression sub_class_of','sub_class_of_optional',2,'p_start','osa.py',69),
  ('sub_class_of_optional -> disjoint_classes','sub_class_of_optional',1,'p_start','osa.py',70),
  ('sub_class_of_optional -> empty','sub_class_of_optional',1,'p_start','osa.py',71),
  ('equivalent_to -> KEYWORD_EQUIVALENTTO TWOPOINTS equivalent_to_expression','equivalent_to',3,'p_start','osa.py',73),
  ('equivalent_to -> empty','equivalent_to',1,'p_start','osa.py',74),
  ('equivalent_to_expression -> CLASS KEYWORD LPAREN PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE LCOLCH SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL RCOLCH RPAREN','equivalent_to_expression',14,'p_start','osa.py',78),
  ('equivalent_to_expression -> CLASS KEYWORD LPAREN PROPERTY KEYWORD CLASS RPAREN equivalent_to_expression','equivalent_to_expression',8,'p_start','osa.py',79),
  ('equivalent_to_expression -> CLASS KEYWORD LPAREN PROPERTY KEYWORD LPAREN property_expression equivalent_to_expression','equivalent_to_expression',8,'p_start','osa.py',80),
  ('equivalent_to_expression -> KEYWORD LPAREN PROPERTY KEYWORD LPAREN property_expression equivalent_to_expression','equivalent_to_expression',7,'p_start','osa.py',81),
  ('equivalent_to_expression -> KEYWORD LPAREN PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE RPAREN equivalent_to_expression','equivalent_to_expression',9,'p_start','osa.py',82),
  ('equivalent_to_expression -> SPECIAL_SYMBOL CLASS equivalent_to_expression','equivalent_to_expression',3,'p_start','osa.py',83),
  ('equivalent_to_expression -> SPECIAL_SYMBOL CLASS SPECIAL_SYMBOL equivalent_to_expression','equivalent_to_expression',4,'p_start','osa.py',84),
  ('equivalent_to_expression -> equivalent_to_enumerated_expression','equivalent_to_expression',1,'p_start','osa.py',85),
  ('equivalent_to_expression -> equivalent_to_nested_expression','equivalent_to_expression',1,'p_start','osa.py',86),
  ('equivalent_to_expression -> equivalent_to_covered_expression','equivalent_to_expression',1,'p_start','osa.py',87),
  ('equivalent_to_expression -> empty','equivalent_to_expression',1,'p_start','osa.py',88),
  ('equivalent_to_enumerated_expression -> LKEY INSTANCE SPECIAL_SYMBOL','equivalent_to_enumerated_expression',3,'p_start','osa.py',90),
  ('equivalent_to_enumerated_expression -> INSTANCE SPECIAL_SYMBOL','equivalent_to_enumerated_expression',2,'p_start','osa.py',91),
  ('equivalent_to_enumerated_expression -> INSTANCE RKEY','equivalent_to_enumerated_expression',2,'p_start','osa.py',92),
  ('equivalent_to_enumerated_expression -> empty','equivalent_to_enumerated_expression',1,'p_start','osa.py',93),
  ('equivalent_to_nested_expression -> CLASS KEYWORD equivalent_to_nested_expression','equivalent_to_nested_expression',3,'p_start','osa.py',95),
  ('equivalent_to_nested_expression -> KEYWORD LPAREN PROPERTY KEYWORD equivalent_to_nested_expression','equivalent_to_nested_expression',5,'p_start','osa.py',96),
  ('equivalent_to_nested_expression -> LPAREN PROPERTY KEYWORD CLASS RPAREN equivalent_to_nested_expression','equivalent_to_nested_expression',6,'p_start','osa.py',97),
  ('equivalent_to_nested_expression -> <empty>','equivalent_to_nested_expression',0,'p_start','osa.py',98),
  ('individuals -> KEYWORD_INDIVIDUALS TWOPOINTS INDIVIDUAL individuals','individuals',4,'p_start','osa.py',100),
  ('individuals -> SPECIAL_SYMBOL INDIVIDUAL individuals','individuals',3,'p_start','osa.py',101),
  ('individuals -> empty','individuals',1,'p_start','osa.py',102),
  ('property_expression -> PROPERTY KEYWORD CLASS SPECIAL_SYMBOL property_expression','property_expression',5,'p_start','osa.py',104),
  ('property_expression -> PROPERTY KEYWORD NUMERAL NAMESPACE TWOPOINTS TYPE property_expression','property_expression',7,'p_start','osa.py',105),
  ('property_expression -> PROPERTY KEYWORD LPAREN property_expression','property_expression',4,'p_start','osa.py',106),
  ('property_expression -> PROPERTY KEYWORD property_expression_closure','property_expression',3,'p_start','osa.py',107),
  ('property_expression -> PROPERTY KEYWORD CLASS RPAREN property_expression','property_expression',5,'p_start','osa.py',108),
  ('property_expression -> PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL','property_expression',9,'p_start','osa.py',109),
  ('property_expression -> PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL','property_expression',8,'p_start','osa.py',110),
  ('property_expression -> PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE RPAREN','property_expression',6,'p_start','osa.py',111),
  ('property_expression -> RPAREN property_expression','property_expression',2,'p_start','osa.py',112),
  ('property_expression -> empty','property_expression',1,'p_start','osa.py',113),
  ('equivalent_to_covered_expression -> CLASS KEYWORD equivalent_to_covered_expression','equivalent_to_covered_expression',3,'p_start','osa.py',115),
  ('equivalent_to_covered_expression -> CLASS equivalent_to_covered_expression','equivalent_to_covered_expression',2,'p_start','osa.py',116),
  ('equivalent_to_covered_expression -> KEYWORD CLASS','equivalent_to_covered_expression',2,'p_start','osa.py',117),
  ('equivalent_to_covered_expression -> empty','equivalent_to_covered_expression',1,'p_start','osa.py',118),
  ('disjoint_classes -> KEYWORD_DISJOINT TWOPOINTS CLASS disjoint_classes','disjoint_classes',4,'p_start','osa.py',120),
  ('disjoint_classes -> SPECIAL_SYMBOL CLASS disjoint_classes','disjoint_classes',3,'p_start','osa.py',121),
  ('disjoint_classes -> empty','disjoint_classes',1,'p_start','osa.py',122),
  ('property_expression_closure -> LPAREN CLASS property_expression_closure','property_expression_closure',3,'p_start','osa.py',124),
  ('property_expression_closure -> KEYWORD CLASS property_expression_closure','property_expression_closure',3,'p_start','osa.py',125),
  ('property_expression_closure -> KEYWORD CLASS RPAREN property_expression','property_expression_closure',4,'p_start','osa.py',126),
  ('property_expression_closure -> empty','property_expression_closure',1,'p_start','osa.py',127),
  ('nested_descriptions_class -> KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals','nested_descriptions_class',5,'p_start','osa.py',129),
  ('nested_descriptions_class -> KEYWORD_CLASS TWOPOINTS CLASS equivalent_to','nested_descriptions_class',4,'p_start','osa.py',130),
  ('empty -> <empty>','empty',0,'p_empty','osa.py',156),
]
