import pytest
from project1 import redact_pipeline


def test_pipeline():
    unredacted_txt = """Barack Obama was the 44th president of the United States, and the first African American to serve in the office. First elected to the presidency in 2008,  won a second term in 2012. He born in Honolulu in 1961, Barack Obama went on to become President of the Harvard Law Review and a U.S. senator representing Illinois. In 2008, Barack Obama  was elected President of the United States, becoming the first African-American commander-in-chief. Barack Obama served two terms as the 44th president of the United States.Barack Hussein Obama II was born in Honolulu, Hawaii, on August 4, 1961. His mother, Ann Dunham, was born on an Army base in Wichita, Kansas, during World War II. After the Japanese attack on Pearl Harbor, Dunham's father, Stanley, enlisted in the military and marched across Europe in General George Patton's army. Dunham's mother, Madelyn, went to work on a bomber assembly line. After the war, the couple studied on the G.I. Bill, bought a house through the Federal Housing Program and, after several moves, ended up in Hawaii.Obama's father, Barack Obama Sr., was born of Luo ethnicity in Nyanza Province, Kenya. Obama Sr. grew up herding goats in Africa and, eventually earned a scholarship that allowed him to leave Kenya and pursue his dreams of going to college in Hawaii. While studying at the University of Hawaii at Manoa, Barack Obama Sr. met fellow student Ann Dunham, and they married on February 2, 1961.

Check to see if the dates are redacted :
February 2, 1971
March 10, 2009
January 15, 1990
June 3, 1972"""

    got_redacted_txt, got_stats = redact_pipeline(
        unredacted_txt,
        redacts={
            'names': True,
            'genders': True,
            'phones': True,
            'dates': True,
            'address': True},
        concepts=['kids'])

    want_redacted_txt = """████████████ was the 44th president of █████████████████, and the first ████████████████ to serve in the office. First elected to the presidency in ████, won a second term in ████. ██ born in ████████ in ████, ████████████ went on to become President of ██████████████████████ and a ████ senator representing ████████. In ████, ████████████ was elected President of █████████████████, becoming the first ████████████████ commander-in-chief. ████████████ served two terms as the 44th president of █████████████████.███████████████████████ was born in ████████, ██████, on ██████████████. ███ ██████, ██████████, was born on an ████ base in ███████, ██████, during World War II. After the ████████ attack on Pearl Harbor, ████████ ██████, ███████, enlisted in the military and marched across Europe in General ███████████████ army. ████████ ██████, ███████, went to work on a bomber assembly line. After the war, the couple studied on the █████████, bought a house through ███████████████████████████ and, after several moves, ended up in ██████.███████ ██████, ████████████████, was born of ███ ethnicity in ███████████████, █████. █████████ grew up herding goats in Africa and, eventually earned a scholarship that allowed ███ to leave █████ and pursue ███ dreams of going to college in ██████. While studying at ███████████████████████████ █████, ████████████████ met fellow student ██████████, and they married on ████████████████.

Check to see if the dates are redacted :
█████████████████████████████████████████████████████████████"""

    want_stats = f"""NAME: 41 redactions
\tStart: 0, End: 12 => Barack Obama
\tStart: 39, End: 56 => the United States
\tStart: 72, End: 88 => African American
\tStart: 192, End: 200 => Honolulu
\tStart: 210, End: 222 => Barack Obama
\tStart: 254, End: 276 => the Harvard Law Review
\tStart: 283, End: 287 => U.S.
\tStart: 309, End: 317 => Illinois
\tStart: 328, End: 340 => Barack Obama
\tStart: 366, End: 383 => the United States
\tStart: 404, End: 420 => African-American
\tStart: 441, End: 453 => Barack Obama
\tStart: 496, End: 513 => the United States
\tStart: 514, End: 537 => Barack Hussein Obama II
\tStart: 550, End: 558 => Honolulu
\tStart: 560, End: 566 => Hawaii
\tStart: 599, End: 609 => Ann Dunham
\tStart: 626, End: 630 => Army
\tStart: 639, End: 646 => Wichita
\tStart: 648, End: 654 => Kansas
\tStart: 687, End: 695 => Japanese
\tStart: 720, End: 728 => Dunham's
\tStart: 737, End: 744 => Stanley
\tStart: 808, End: 823 => George Patton's
\tStart: 830, End: 838 => Dunham's
\tStart: 847, End: 854 => Madelyn
\tStart: 937, End: 946 => G.I. Bill
\tStart: 971, End: 998 => the Federal Housing Program
\tStart: 1037, End: 1043 => Hawaii
\tStart: 1044, End: 1051 => Obama's
\tStart: 1060, End: 1076 => Barack Obama Sr.
\tStart: 1090, End: 1093 => Luo
\tStart: 1107, End: 1122 => Nyanza Province
\tStart: 1124, End: 1129 => Kenya
\tStart: 1131, End: 1140 => Obama Sr.
\tStart: 1236, End: 1241 => Kenya
\tStart: 1287, End: 1293 => Hawaii
\tStart: 1313, End: 1340 => the University of Hawaii at
\tStart: 1341, End: 1346 => Manoa
\tStart: 1348, End: 1364 => Barack Obama Sr.
\tStart: 1384, End: 1394 => Ann Dunham
GENDER: 8 redactions
\tStart: 181, End: 183 => He
\tStart: 587, End: 590 => His
\tStart: 591, End: 597 => mother
\tStart: 729, End: 735 => father
\tStart: 839, End: 845 => mother
\tStart: 1052, End: 1058 => father
\tStart: 1223, End: 1226 => him
\tStart: 1253, End: 1256 => his
DATE: 7 redactions
\tStart: 148, End: 152 => 2008
\tStart: 175, End: 179 => 2012
\tStart: 204, End: 208 => 1961
\tStart: 322, End: 326 => 2008
\tStart: 571, End: 585 => August 4, 1961
\tStart: 1416, End: 1432 => February 2, 1961
\tStart: 1476, End: 1537 => February 2, 1971
March 10, 2009
January 15, 1990
June 3, 1972
PHONENUM: 0 redactions
ADDRESS: 0 redactions
CONCEPT: 0 redactions"""

    assert got_redacted_txt == want_redacted_txt
    assert got_stats == want_stats
