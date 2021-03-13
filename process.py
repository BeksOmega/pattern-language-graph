# Processes a text file version of A Pattern Language by Christopher Alexander
# et al. and outputs a graphml file mapping the relationships between
# patterns.
# The names of the input file and the output file must be passed as arguments.

import re
import sys
from pygraphml import GraphMLParser
from pygraphml import Graph

# Pattern IDs and names.
patterns = [
  (1, 'INDEPENDENT REGIONS'),
  (2, 'THE DISTRIBUTION OF TOWNS'),
  (3, 'CITY COUNTRY FINGERS'),
  (4, 'AGRICULTURAL VALLEYS'),
  (5, 'LACE OF COUNTRY STREETS'),
  (6, 'COUNTRY TOWNS'),
  (7, 'THE COUNTRYSIDE'),
  (8, 'MOSAIC OF SUBCULTURES'),
  (9, 'SCATTERED WORK'),
  (10, 'MAGIC OF THE CITY'),
  (11, 'LOCAL TRANSPORT AREAS'),
  (12, 'COMMUNITY OF 7000'),
  (13, 'SUBCULTURE BOUNDARY'),
  (14, 'IDENTIFIABLE NEIGHBORHOOD'),
  (15, 'NEIGHBORHOOD BOUNDARY'),
  (16, 'WEB OF PUBLIC TRANSPORTATION'),
  (17, 'RING ROADS'),
  (18, 'NETWORK OF LEARNING'),
  (19, 'WEB OF SHOPPING'),
  (20, 'MINI-BUSES'),
  (21, 'FOUR-STORY LIMIT'),
  (22, 'NINE PER CENT PARKING'),
  (23, 'PARALLEL ROADS'),
  (24, 'SACRED SITES'),
  (25, 'ACCESS TO WATER'),
  (26, 'LIFE CYCLE'),
  (27, 'MEN AND WOMEN'),
  (28, 'ECCENTRIC NUCLEUS'),
  (29, 'DENSITY RINGS'),
  (30, 'ACTIVITY NODES'),
  (31, 'PROMENADE'),
  (32, 'SHOPPING STREET'),
  (33, 'NIGHT LIFE'),
  (34, 'INTERCHANGE'),
  (35, 'HOUSEHOLD MIX'),
  (36, 'DEGREES OF PUBLICNESS'),
  (37, 'HOUSE CLUSTER'),
  (38, 'ROW HOUSES'),
  (39, 'HOUSING HILL'),
  (40, 'OLD PEOPLE EVERYWHERE'),
  (41, 'WORK COMMUNITY'),
  (42, 'INDUSTRIAL RIBBON'),
  (43, 'UNIVERSITY AS A MARKETPLACE'),
  (44, 'LOCAL TOWN HALL'),
  (45, 'NECKLACE OF COMMUNITY PROJECTS'),
  (46, 'MARKET OF MANY SHOPS'),
  (47, 'HEALTH CENTER'),
  (48, 'HOUSING IN BETWEEN'),
  (49, 'LOOPED LOCAL ROADS'),
  (50, 'T JUNCTIONS'),
  (51, 'GREEN STREETS'),
  (52, 'NETWORK OF PATHS AND CARS'),
  (53, 'MAIN GATEWAYS'),
  (54, 'ROAD CROSSING'),
  (55, 'RAISED WALK'),
  (56, 'BIKE PATHS AND RACKS'),
  (57, 'CHILDREN IN THE CITY'),
  (58, 'CARNIVAL'),
  (59, 'QUIET BACKS'),
  (60, 'ACCESSIBLE GREEN'),
  (61, 'SMALL PUBLIC SQUARES'),
  (62, 'HIGH PLACES'),
  (63, 'DANCING IN THE STREET'),
  (64, 'POOLS AND STREAMS'),
  (65, 'BIRTH PLACES'),
  (66, 'HOLY GROUND'),
  (67, 'COMMON LAND'),
  (68, 'CONNECTED PLAY'),
  (69, 'PUBLIC OUTDOOR ROOM'),
  (70, 'GRAVE SITES'),
  (71, 'STILL WATER'),
  (72, 'LOCAL SPORTS'),
  (73, 'ADVENTURE PLAYGROUND'),
  (74, 'ANIMALS'),
  (73, 'THE FAMILY'),
  (76, 'HOUSE FOR A SMALL FAMILY'),
  (77, 'HOUSE FOR A COUPLE'),
  (78, 'HOUSE FOR ONE PERSON'),
  (79, 'YOUR OWN HOME'),
  (80, 'SELF-GOVERNING WORKSHOPS AND OFFICES'),
  (81, 'SMALL SERVICES WITHOUT RED TAPE'),
  (82, 'OFFICE CONNECTIONS'),
  (83, 'MASTER AND APPRENTICES'),
  (84, 'TEENAGE SOCIETY'),
  (85, 'SHOPFRONT SCHOOLS'),
  (86, "CHILDREN'S HOME"),
  (87, 'INDIVIDUALLY OWNED SHOPS'),
  (88, 'STREET CAFE'),
  (89, 'CORNER GROCERY'),
  (90, 'BEER HALL'),
  (91, "TRAVELER'S INN"),
  (92, 'BUS STOP'),
  (93, 'FOOD STANDS'),
  (94, 'SLEEPING IN PUBLIC'),
  (95, 'BUILDING COMPLEX'),
  (96, 'NUMBER OF STORIES'),
  (97, 'SHIELDED PARKING'),
  (98, 'CIRCULATION REALMS'),
  (99, 'MAIN BUILDING'),
  (100, 'PEDESTRIAN STREET'),
  (101, 'BUILDING THOROUGHFARE'),
  (102, 'FAMILY OF ENTRANCES'),
  (103, 'SMALL PARKING LOTS'),
  (104, 'SITE REPAIR'),
  (105, 'SOUTH FACING OUTDOORS'),
  (106, 'POSITIVE OUTDOOR SPACE'),
  (107, 'WINGS OF LIGHT'),
  (108, 'CONNECTED BUILDINGS'),
  (109, 'LONG THIN HOUSE'),
  (110, 'MAIN ENTRANCE'),
  (111, 'HALF-HIDDEN GARDEN'),
  (112, 'ENTRANCE TRANSITION'),
  (113, 'CAR CONNECTION'),
  (114, 'HIERARCHY OF OPEN SPACE'),
  (115, 'COURTYARDS WHICH LIVE'),
  (116, 'CASCADE OF ROOFS'),
  (117, 'SHELTERING ROOF'),
  (118, 'ROOF GARDEN'),
  (119, 'ARCADES'),
  (120, 'PATHS AND GOALS'),
  (121, 'PATH SHAPE'),
  (122, 'BUILDING FRONTS'),
  (123, 'PEDESTRIAN DENSITY'),
  (124, 'ACTIVITY POCKETS'),
  (125, 'STAIR SEATS'),
  (126, 'SOMETHING ROUGHLY IN THE MIDDLE'),
  (127, 'INTIMACY GRADIENT'),
  (128, 'INDOOR SUNLIGHT'),
  (129, 'COMMON AREAS AT THE HEART'),
  (130, 'ENTRANCE ROOM'),
  (131, 'THE FLOW THROUGH ROOMS'),
  (132, 'SHORT PASSAGES'),
  (133, 'STAIRCASE AS A STAGE'),
  (134, 'ZEN VIEW'),
  (135, 'TAPESTRY OF LIGHT AND DARK'),
  (136, "COUPLE'S REALM"),
  (137, "CHILDREN'S REALM"),
  (138, 'SLEEPING TO THE EAST'),
  (139, 'FARMHOUSE KITCHEN'),
  (140, 'PRIVATE TERRACE ON THE STREET'),
  (141, "A ROOM OF ONE's OWN"),
  (142, 'SEQUENCE OF SITTING SPACES'),
  (143, 'BED CLUSTER'),
  (144, 'BATHING ROOM'),
  (145, 'BULK STORAGE'),
  (146, 'FLEXIBLE OFFICE SPACE'),
  (147, 'COMMUNAL EATING'),
  (148, 'SMALL WORK GROUPS'),
  (149, 'RECEPTION WELCOMES YOU'),
  (150, 'A PLACE TO WAIT'),
  (151, 'SMALL MEETING ROOMS'),
  (152, 'HALF-PRIVATE OFFICE'),
  (153, 'ROOMS TO RENT'),
  (154, "TEENAGER'S COTTAGE"),
  (155, 'OLD AGE COTTAGE'),
  (156, 'SETTLED WORK'),
  (157, 'HOME WORKSHOP'),
  (158, 'OPEN STAIRS'),
  (159, 'LIGHT ON TWO SIDES OF EVERY ROOM'),
  (160, 'BUILDING EDGE'),
  (161, 'SUNNY PLACE'),
  (162, 'NORTH FACE'),
  (163, 'OUTDOOR ROOM'),
  (164, 'STREET WINDOWS'),
  (165, 'OPENING TO THE STREET'),
  (166, 'GALLERY SURROUND'),
  (167, 'SIX-FOOT BALCONY'),
  (168, 'CONNECTION TO THE EARTH'),
  (169, 'TERRACED SLOPE'),
  (170, 'FRUIT TREES'),
  (171, 'TREE PLACES'),
  (172, 'GARDEN GROWING WILD'),
  (173, 'GARDEN WALL'),
  (174, 'TRELLISED WALK'),
  (175, 'GREENHOUSE'),
  (176, 'GARDEN SEAT'),
  (177, 'VEGETABLE GARDEN'),
  (178, 'COMPOST'),
  (179, 'ALCOVES'),
  (180, 'WINDOW PLACE'),
  (181, 'THE FIRE'),
  (182, 'EATING ATMOSPHERE'),
  (183, 'WORKSPACE ENCLOSURE'),
  (184, 'COOKING LAYOUT'),
  (185, 'SITTING CIRCLE'),
  (186, 'COMMUNAL SLEEPING'),
  (187, 'MARRIAGE BED'),
  (188, 'BED ALCOVE'),
  (189, 'DRESSING ROOMS'),
  (190, 'CEILING HEIGHT VARIETY'),
  (191, 'THE SHAPE OF INDOOR SPACE'),
  (192, 'WINDOWS OVERLOOKING LIFE'),
  (193, 'HALF-OPEN WALL'),
  (194, 'INTERIOR WINDOWS'),
  (195, 'STAIRCASE VOLUME'),
  (196, 'CORNER DOORS'),
  (197, 'THICK WALLS'),
  (198, 'CLOSETS BETWEEN ROOMS'),
  (199, 'SUNNY COUNTER'),
  (200, 'OPEN SHELVES'),
  (201, 'WAIST-HIGH SHELF'),
  (202, 'BUILT-IN SEATS'),
  (203, 'CHILD CAVES'),
  (204, 'SECRET PLACE'),
  (205, 'STRUCTURE FOLLOWS SOCIAL SPACES'),
  (206, 'EFFICIENT STRUCTURE'),
  (207, 'GOOD MATERIALS'),
  (208, 'GRADUAL STIFFENING'),
  (209, 'ROOF LAYOUT'),
  (210, 'FLOOR AND CEILING LAYOUT'),
  (201, 'THICKENING THE OUTER WALLS'),
  (212, 'COLUMNS AT THE CORNERS'),
  (213, 'FINAL COLUMN DISTRIBUTION'),
  (214, 'ROOT FOUNDATIONS'),
  (215, 'GROUND FLOOR SLAB'),
  (216, 'BOX COLUMNS'),
  (217, 'PERIMETER BEAMS'),
  (218, 'WALL MEMBRANES'),
  (219, 'FLOOR-CEILING VAULTS'),
  (220, 'ROOF VAULTS'),
  (221, 'NATURAL DOORS AND WINDOWS'),
  (222, 'LOW SILL'),
  (223, 'DEEP REVEALS'),
  (224, 'LOW DOORWAY'),
  (225, 'FRAMES AS THICKENED EDGES'),
  (226, 'COLUMN PLACE'),
  (227, 'COLUMN CONNECTIONS'),
  (228, 'STAIR VAULT'),
  (229, 'DUCT SPACE'),
  (230, 'RADIANT HEAT'),
  (231, 'DORMER WINDOWS'),
  (232, 'ROOF CAPS'),
  (233, 'FLOOR SURFACE'),
  (234, 'LAPPED OUTSIDE WALLS'),
  (235, 'SOFT INSIDE WALLS'),
  (236, 'WINDOWS WHICH OPEN WIDE'),
  (237, 'SOLID DOORS WITH GLASS'),
  (238, 'FILTERED LIGHT'),
  (239, 'SMALL PANES'),
  (240, 'HALF-INCH TRIM'),
  (241, 'SEAT SPOTS'),
  (242, 'FRONT DOOR BENCH'),
  (243, 'SITTING WALL'),
  (244, 'CANVAS ROOFS'),
  (245, 'RAISED FLOWERS'),
  (246, 'CLIMBING PLANTS'),
  (247, 'PAVING WITH CRACKS BETWEEN THE STONES'),
  (248, 'SOFT TILE AND BRICK'),
  (249, 'ORNAMENT'),
  (250, 'WARM COLORS'),
  (251, 'DIFFERENT CHAIRS'),
  (252, 'POOLS OF LIGHT'),
  (253, 'THINGS FROM YOUR LIFE')]

# Ranges defining the major sections of the book.
sections = [
  ('TOWNS', range(1, 95)),
  ('BUILDINGS', range(95, 205)),
  ('CONSTRUCTION', range(205, 254))]

# Ranges defining subsections of the book (names are unofficial).
subsections = [
  ('REGIONS', range(1, 8)),
  ('MAJOR CITY STRUCTURES', range(8, 12)),
  ('COMMUNITY BOUNDARIES', range(12, 16)),
  ('COMMUNITY CONNECTIONS', range(16, 21)),
  ('COMMUNITY CHARACTER', range(21, 28)),
  ('LOCAL CENTERS', range(28, 35)),
  ('HOUSE CLUSTERS', range(35, 41)),
  ('WORK COMMUNITIES', range(41, 49)),
  ('ROADS AND PATHS', range(49, 58)),
  ('COMMON LAND', range(58, 67)),
  ('LOCAL COMMON LAND', range(67, 75)),
  ('THE FAMILY', range(75, 80)),
  ('WORK GROUPS', range(80, 87)),
  ('LOCAL SHOPS', range(87, 95)),
  ('BUILDING ARRANGEMENT', range(95, 104)),
  ('BUILDING LOCATION', range(104, 110)),
  ('BUILDING SHAPE', range(110, 119)),
  ('PATHS', range(119, 127)),
  ('GRADIENTS OF SPACE', range(127, 136)),
  ('HOUSE ROOMS', range(136, 146)),
  ('WORK ROOMS', range(146, 153)),
  ('OUTBUILDINGS', range(153, 159)),
  ('ROOM EDGES', range(159, 169)),
  ('GARDENS', range(169, 179)),
  ('ALCOVES', range(179, 190)),
  ('ROOM SHAPES', range(190, 197)),
  ('WALLS', range(197, 205)),
  ('PHILOSOPHY OF STRUCTURE', range(205, 209)),
  ('STRUCTURAL LAYOUT', range(209, 214)),
  ('STRUCTURAL FRAME', range(214, 221)),
  ('OPENINGS', range(221, 226)),
  ('STRUCTURAL SUBSIDIARIES', range(26, 233)),
  ('SURFACES', range(233, 241)),
  ('OUTDOOR DETAILS', range(241, 249)),
  ('ORNAMENTATION', range(249, 254))]

# A dictionary mapping pattern IDs to nodes.
nodesDict = {}

def removeDuplicateHeadings(lines):
  heading = None;
  headIndex = -1;
  nlines = []
  for line in lines:
    match = re.match(r'\f[\SA-Z0-9]+ ([A-Z0-9 ]+)(\**)\n', line)
    if match:
      if heading != None and heading in match.group(1):
        stars = re.match(r'[^*]*(\**)', nlines[headIndex])
        nlines[headIndex] = '[[' + match.group(1).strip() + stars.group(1) + ']]'
      else:
        heading = match.group(1).strip()
        headIndex = len(nlines)
        nlines.append('[[' + heading + match.group(2) +']]')
    else:
       nlines.append(line)
  return nlines

# Manual fixes for headings.
def fixHeadings(lines):
  nlines = []
  for line in lines:
    if '[[CONNECTED BUITDINGS]]' in line:
      nlines.append('[[CONNECTED BUILDINGS]]')
    elif '[[3 CAR CONNECTION]]' in line:
      nlines.append('[[CAR CONNECTION]]')
    elif '[[ROQF VAULTS]]' in line:
      nlines.append('[[ROOF VAULTS]]')
    elif '[[DERP REVEALS]]' in line:
      nlines.append('[[DEEP REVEALS]]')
    else:
      nlines.append(line)
  return nlines

def removeSectionTitles(lines):
  nlines = []
  for line in lines:
    # Remove TOWNS, BUILDINGS, or CONSTRUCTION
    match = re.match(r'\f+[a-zA-Z0-9]+\n', line)
    if not match:
      nlines.append(line)
  return nlines

def removePageNumbers(lines):
  nlines = []
  for line in lines:
    match = re.match(r'\d+\n', line)
    if not match:
       nlines.append(line)
  return nlines

# Matches our special heading format, not default headings.
def isHeading(line):
  return re.match(r'\[\[([^*]*)(\**)\]\]', line)

def removeWhiteSpace(lines):
  nlines = []
  for line in lines:
    if isHeading(line):
      nlines.append(line)
    else:
      nlines.append(re.sub('\s', '', line))
  return nlines

def squishParagraphs(lines):
  latestPara = -1
  nlines = []
  for line in lines:
    if isHeading(line):
      nlines.append(line)
    elif line == '':
      nlines.append(line)
      latestPara = -1
    elif latestPara == -1:
      latestPara = len(nlines)
      nlines.append(line)
    else:
      nlines[latestPara] += line
  return nlines

def moveSmallParagraphs(lines):
  latestPara = -1
  nlines = []
  for line in lines:
    if len(line) > 20 or isHeading(line):
      latestPara = len(nlines)
      nlines.append(line)
    elif line == '':
      nlines.append(line)
    else:
      nlines[latestPara] += line
  return nlines

def removeBlankLines(lines):
  nlines = []
  for i, line in enumerate(lines):
    if line != '':
      nlines.append(line)
      nlines.append('')
  return nlines

def addNodes(g):
  for (num, name) in patterns:
    node = g.add_node(num)
    node['name'] = name
    node['section'] = next((s[0] for s in sections if num in s[1]), None)
    node['subsection'] = next((s[0] for s in subsections if num in s[1]), None)
    nodesDict[num] = node;

def setStars(lines):
  notFound = {p[0] for p in patterns}
  for line in lines:
    match = isHeading(line)
    if match:
      group = match.group(1)
      pattern = next((p for p in patterns if group in p[1]), None)
      if pattern == None:
        print(f'Could not find pattern for {group}')
      else:
        nodesDict[pattern[0]]['stars'] = len(match.group(2))
        if pattern[0] in notFound:
          notFound.remove(pattern[0])
  for pattern in notFound:
    nodesDict[pattern]['stars'] = 0

def addEdges(g, lines):
  for i, line in enumerate(lines):
    match = isHeading(line)
    if match:
      group = match.group(1)
      pattern = next((p for p in patterns if group in p[1]), None)
      if pattern != None:
        node = nodesDict[pattern[0]]
        for string in re.findall(r'\((\d+)\)', lines[i + 2]):
          if int(string) in nodesDict:
            e = g.add_edge(nodesDict[int(string)], node, True)
            e['origin'] = 'start'
        for string in re.findall(r'\((\d+)\)', lines[i - 2]):
          if int(string) in nodesDict:
            e = g.add_edge(node, nodesDict[int(string)], True)
            e['origin'] = 'end'

def postProcessGraph(g, lines):
  # Add manual fixes here.
  pass
      
# Actually process the file and output the graph.
if len(sys.argv) < 3:
  print('Expected input and output file names')
else:
  with (open(sys.argv[1], 'r')) as f:
    lines = f.readlines()
    lines = removeDuplicateHeadings(lines)
    lines = fixHeadings(lines)
    lines = removeSectionTitles(lines)
    lines = removePageNumbers(lines)
    lines = removeWhiteSpace(lines)
    lines = squishParagraphs(lines)
    lines = moveSmallParagraphs(lines)
    lines = removeBlankLines(lines)
  
    g = Graph()
    addNodes(g)
    setStars(lines)
    addEdges(g, lines)
    postProcessGraph(g, lines)
  
    parser = GraphMLParser()
    parser.write(g, sys.argv[2])

