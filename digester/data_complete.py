"""
Complete Teaching Data Modules
================================
Consolidated data module containing three comprehensive educational databases:
- TEACHING_INSIGHTS_COMPLETE: Pedagogical insights and misconceptions (31 topics)
- RISA_DIALOGUES_COMPLETE: Student-teacher dialogue examples (30 topics)
- LEVELED_PROBLEMS_COMPLETE: Graduated problem sets (30 topics)

Includes helper functions for data retrieval and searching across all three databases.
"""

TEACHING_INSIGHTS_COMPLETE = {
    "ratios and rates": {
        "grade": 6,
        "misconceptions": [
            "Students think ratios and fractions are identical, not recognizing that ratios compare two separate quantities rather than describing a part-to-whole relationship",
            "Students believe the order of a ratio doesn't matter (3:4 equals 4:3), not understanding that ratios express specific directional comparisons",
            "Students confuse rate with ratio, failing to recognize that rates always compare two quantities with different units",
            "Students think equivalent ratios must have the same numbers, not recognizing that multiplying both terms by the same factor creates equivalent ratios"
        ],
        "differentiation": {
            "emergent": "Use concrete manipulatives like counters or blocks to physically build ratios. Create visual tape diagrams showing two distinct quantities side-by-side. Practice with real objects first (3 red markers to 4 blue markers) before abstract notation. Use consistent language: 'For every 3, there are 4.'",
            "ell": "Provide sentence frames: 'A ratio compares ___ to ___.' 'The ratio of ___ to ___ is ___.' Use visual ratio cards with images and numerals together. Pre-teach vocabulary: ratio, quantity, compare. Partner with bilingual peer for key concepts.",
            "extending": "Challenge with three-part ratios (boys:girls:teachers). Present real-world scenarios requiring ratio analysis (recipes scaling, map scales). Have students generate multiple equivalent ratios and explain the multiplicative relationship. Ask 'What if the ratio doubled?'"
        },
        "essential_understandings": [
            "A ratio is a multiplicative comparison between two quantities that can be expressed in multiple forms (3:4, 3 to 4, 3/4, or 'for every 3 of one quantity, there are 4 of another')",
            "Equivalent ratios are created by multiplying or dividing both terms by the same non-zero number, maintaining the same multiplicative relationship",
            "Ratios are different from fractions because they compare two quantities rather than describing parts of a whole",
            "Rates are special ratios that compare quantities with different units (e.g., miles per hour, cost per item)"
        ]
    },
    "division of fractions": {
        "grade": 6,
        "misconceptions": [
            "Students think dividing by a fraction means dividing by the numerator and denominator separately, leading to incorrect algorithms",
            "Students believe 'dividing makes things smaller' always applies, missing that dividing by a fraction less than 1 makes the result larger",
            "Students invert the dividend instead of the divisor, showing confusion about which fraction changes in the invert-and-multiply algorithm",
            "Students see division of fractions as an abstract rule without understanding the underlying concept of 'how many groups of this size fit into that quantity'"
        ],
        "differentiation": {
            "emergent": "Use visual models like area rectangles or fraction bars to show division as grouping. Start with concrete problems: 'If you have 2 pounds of almonds and put 1/4 pound in each bag, how many bags?' Use length models on number lines. Build to the algorithm only after conceptual understanding is solid.",
            "ell": "Use repeated subtraction language: 'How many 1/4s fit into 2?' Create anchor charts showing division as 'sharing into groups' versus 'how many groups.' Pre-teach: divisor, dividend, quotient, reciprocal. Use visuals before any symbolic work.",
            "extending": "Present problems requiring division of fractions to fractions (5/6 ÷ 2/3). Have students explain why dividing by 1/2 gives a larger result than the original number. Ask students to create their own word problems and justify solutions using visual models and the algorithm."
        },
        "essential_understandings": [
            "Division of fractions can be understood as 'how many groups of the divisor fit into the dividend' which connects to the invert-and-multiply algorithm",
            "When dividing by a fraction less than 1, the quotient is larger than the dividend (e.g., 2 ÷ 1/4 = 8)",
            "The invert-and-multiply rule works because multiplying by the reciprocal is equivalent to the division operation",
            "Division of fractions follows the same structure as division of whole numbers but requires understanding of fraction multiplication"
        ]
    },
    "positive and negative numbers (number line)": {
        "grade": 6,
        "misconceptions": [
            "Students think a negative number is just the opposite symbol of a positive (treating -5 as 'wrong' rather than a position on a number line)",
            "Students believe negative numbers are smaller in quantity but don't understand they represent positions in opposite direction from zero",
            "Students confuse the minus sign as always meaning subtraction, not recognizing it can indicate a negative number itself",
            "Students think negative numbers aren't 'real' or can't be used in practical applications, not connecting them to situations like debt, temperature below zero, or elevation below sea level"
        ],
        "differentiation": {
            "emergent": "Use physical number lines (tape on floor or wall) where students walk to positive and negative positions. Start with real contexts: temperature changes, elevation, bank account changes. Use two-color counters or chips (red for negative, yellow for positive) to represent quantities. Build the horizontal number line connection before addressing operations.",
            "ell": "Create bilingual anchor charts showing positions and contexts for positive/negative numbers. Use consistent language: 'negative means opposite direction from zero' or 'below zero.' Pre-teach: positive, negative, opposite, integer. Provide sentence frames: 'A negative number means ___.' Use pictures with both symbols and meanings.",
            "extending": "Have students explore absolute value intuitively ('distance from zero'). Present multi-step scenarios with direction changes (moving up 5 floors, then down 3 floors). Ask students to generate real-world examples and explain why both positive and negative numbers are necessary."
        },
        "essential_understandings": [
            "Positive and negative numbers are positions on a number line where zero is the reference point, with negatives extending left (or down) and positives extending right (or up)",
            "Positive and negative numbers model real situations with opposite directions: gain/loss, above/below, right/left, forward/backward",
            "Two integers that are opposite (like 5 and -5) are equidistant from zero on a number line",
            "The magnitude of a number (absolute value) tells its distance from zero, regardless of direction"
        ]
    },
    "absolute value": {
        "grade": 6,
        "misconceptions": [
            "Students think absolute value means 'make it negative' or 'take the opposite,' reversing the actual definition of distance from zero",
            "Students believe absolute value always makes answers positive without understanding why (the 'distance' interpretation), treating it as a mechanical rule",
            "Students confuse absolute value notation |x| with parentheses or other grouping symbols, not recognizing its specific meaning",
            "Students think absolute value is only useful for negative numbers, not recognizing it applies equally to positive numbers"
        ],
        "differentiation": {
            "emergent": "Use a number line to show absolute value as distance from zero. Mark two numbers (like -3 and 3) and measure their distance. Say: 'Absolute value is how far a number is from zero.' Use contexts: 'You have $3 in savings or $3 in debt—both are 3 units away from having $0.' Build physical understanding before symbolic work.",
            "ell": "Create visual anchor chart: 'Absolute value means DISTANCE from zero.' Show |number| = distance with arrows pointing from numbers to zero on a number line. Use simplified language: 'How far from zero?' Pre-teach: absolute value, distance, origin. Provide examples with both positive and negative numbers side-by-side.",
            "extending": "Have students explore why |-5| = |5| and explain this relationship. Present comparison problems: 'Which is farther from zero: -8 or 3?' Ask students to apply absolute value to real scenarios (temperature changes, stock price movements) and determine 'distance' from a baseline."
        },
        "essential_understandings": [
            "Absolute value represents the distance a number is from zero on a number line, always resulting in a non-negative value",
            "The absolute value of a positive number is the number itself; the absolute value of a negative number is its opposite",
            "Opposite numbers have the same absolute value (|-a| = |a|) because they are equidistant from zero",
            "Absolute value is a property of magnitude independent of direction, making it useful for measuring distance and comparing sizes"
        ]
    },
    "variables and expressions": {
        "grade": 6,
        "misconceptions": [
            "Students think a variable is just another name for an unknown number, missing that variables can represent a range of values or a changing quantity",
            "Students believe a coefficient (like the 3 in 3x) means addition, interpreting 3x as 3 + x rather than 3 times x",
            "Students think every expression with variables must equal zero or have a single numeric answer, not recognizing expressions represent quantities that depend on the variable's value",
            "Students use letters and numbers interchangeably in algebra, writing 2y = 2y + 1 or similar, not understanding that expressions with different structures have different values"
        ],
        "differentiation": {
            "emergent": "Use concrete models: 'x' = an unknown number of objects in a bag. Write simple expressions with manipulatives: 3 red counters + some yellow (x) = 3 + x. Use area models for multiplication with variables. Start with very accessible contexts before abstract algebra.",
            "ell": "Provide vocabulary anchors: variable, expression, coefficient, term. Create visual examples: 'The cost is 5 dollars per item. If you buy x items, you pay 5x dollars.' Use realistic scenarios to build meaning before notation. Show multiple representations: words, pictures, numbers, symbols.",
            "extending": "Have students write expressions for multi-step processes ('If you start with x dollars, spend $3, then earn $5'). Compare equivalent expressions (2x + 3 vs. 3 + 2x). Present pattern-finding tasks where they identify expressions for the nth term in a sequence."
        },
        "essential_understandings": [
            "A variable is a symbol representing an unknown or changing quantity that can take multiple values",
            "An expression combines variables, numbers, and operations to represent a quantity whose value depends on the variable",
            "In expressions, juxtaposition (like 3x) means multiplication, and terms can be combined if they have the same variable and exponent",
            "Equivalent expressions look different but always produce the same value for any substitution of the variable"
        ]
    },
    "one-step equations and inequalities": {
        "grade": 6,
        "misconceptions": [
            "Students think solving means finding any number that 'works' rather than finding the specific value that makes the statement true, or they provide multiple solutions to an equation",
            "Students apply operations to only one side of an equation, not understanding that equations maintain balance and changes must happen equally on both sides",
            "Students reverse the direction of an inequality without understanding the reasoning (forgetting the rule about multiplying/dividing by negatives), treating inequalities like equations",
            "Students confuse equations (with = sign) and inequalities (with <, >, ≤, ≥), treating them identically in solution methods"
        ],
        "differentiation": {
            "emergent": "Use a balance scale model: objects on the left must equal objects on the right. Show solving as 'what do I need to add or remove to balance?' Start with addition/subtraction only before division. Use concrete counters to represent variables (x = this mystery bag of counters). Build to equations like x + 3 = 7 with physical demonstration.",
            "ell": "Provide sentence frames: 'x equals ___' and 'x is greater than ___.' Create anchor charts showing 'balance' for equations and 'number line' for inequalities. Pre-teach: solve, solution, balanced, inequality. Use repeated examples with consistent structure before varying problems.",
            "extending": "Present multi-step word problems requiring equation setup and solution. Have students explain 'Why do we do the same thing to both sides?' Ask them to verify solutions by substituting back into original equation. Challenge with inequality interpretation: 'x > 5 means all numbers bigger than 5—can you name three?'"
        },
        "essential_understandings": [
            "An equation is a statement that two expressions have equal value; solving means finding the value(s) of the variable that make this true",
            "Inverse operations undo each other, so to solve x + 3 = 7, we subtract 3 from both sides to find x = 4",
            "Equality is preserved when the same operation is applied to both sides of an equation",
            "An inequality shows a relationship where two expressions are not equal; the solution is typically a range of values that satisfy the condition"
        ]
    },
    "area of polygons": {
        "grade": 6,
        "misconceptions": [
            "Students memorize formulas without understanding their basis, unable to apply them to new shapes or explain why the formula works",
            "Students believe the height of a parallelogram must be a slant side, not recognizing that height is the perpendicular distance between parallel sides",
            "Students think the area of a trapezoid is base times height (like a rectangle) without accounting for the two different base lengths",
            "Students confuse area with perimeter, adding dimensions instead of multiplying, or trying to use linear units for an area measurement"
        ],
        "differentiation": {
            "emergent": "Use grid paper to count square units for triangles, parallelograms, and trapezoids. Cut shapes from paper and rearrange pieces (triangle into rectangle, parallelogram into rectangle) to show why formulas work. Build formulas through discovery rather than memorization. Use manipulatives extensively.",
            "ell": "Create bilingual formula cards with visuals: picture of shape, label base and height with perpendicular lines clearly shown, formula, and example. Use consistent language: 'base,' 'height,' 'perpendicular.' Pre-teach shape names in both languages. Show measurement tools and modeling.",
            "extending": "Have students derive area formulas by decomposing shapes (trapezoid = two triangles; parallelogram = rectangle + triangles). Present composite shapes requiring multiple formulas. Ask 'If you double the base, what happens to the area?' and explore proportional reasoning."
        },
        "essential_understandings": [
            "Area measures the amount of space inside a two-dimensional figure, always expressed in square units",
            "The area of a rectangle is length times width; other polygon formulas derive from or relate to this fundamental formula",
            "The height of a triangle or parallelogram is the perpendicular distance from one side (base) to the opposite vertex or side, not necessarily a slant side",
            "The area of a trapezoid accounts for its two parallel bases: A = 1/2 × (base₁ + base₂) × height"
        ]
    },
    "surface area and volume (rectangular prisms)": {
        "grade": 6,
        "misconceptions": [
            "Students confuse surface area (square units, outer covering) with volume (cubic units, inner space), sometimes using the wrong units in answers",
            "Students think surface area is 'length times width times height' (confusing it with volume) or add dimensions instead of computing face areas correctly",
            "Students don't understand that opposite faces of a rectangular prism are congruent and have equal areas, leading to incomplete calculations",
            "Students believe volume must be computed as length × width × height regardless of which dimensions are given, not recognizing these represent three perpendicular measurements"
        ],
        "differentiation": {
            "emergent": "Use physical rectangular prism boxes. Have students wrap them to see surface area ('How much paper covers the outside?') and fill them with unit cubes to understand volume ('How many cubes fit inside?'). Build nets to see all faces. Use consistent color-coding for opposite faces.",
            "ell": "Create anchor charts distinguishing surface area (measured in square units, covering) from volume (measured in cubic units, filling). Use sentence frames: 'Surface area is the ___ of all faces.' 'Volume is how many ___ fit inside.' Pre-teach: prism, surface, volume, unit cube, opposite faces.",
            "extending": "Have students find volume and surface area of the same prism and explain why answers are different. Present problems where dimensions change and ask students to predict how surface area and volume change. Challenge with comparing which uses more material (surface area) versus holds more (volume)."
        },
        "essential_understandings": [
            "Surface area is the total area of all faces of a three-dimensional figure, measured in square units",
            "For a rectangular prism, surface area = 2(lw + lh + wh) because there are three pairs of congruent rectangular faces",
            "Volume is the number of cubic units that fit inside a three-dimensional figure, found by length × width × height",
            "Surface area and volume are independent measurements—a prism can have large surface area with small volume, or vice versa"
        ]
    },
    "statistical questions and distributions": {
        "grade": 6,
        "misconceptions": [
            "Students think any question with 'data' is a statistical question, not recognizing that statistical questions must anticipate variability in responses",
            "Students believe distributions only have one 'answer' or peak, missing that distributions show the spread and frequency of multiple values",
            "Students think the mode or mean is the 'right' answer that everyone should get, not understanding that distributions explain expected variation",
            "Students collect data randomly without considering whether their sample truly represents the population, affecting the validity of distributions"
        ],
        "differentiation": {
            "emergent": "Ask simple statistical questions: 'How many pets do students in our class have?' and 'What is Ms. Johnson's height?' Physically graph data on a line plot or dot plot. Discuss: 'We got different answers—that's what makes it a statistical question.' Use familiar contexts to build understanding of variability.",
            "ell": "Provide sentence frame for statistical questions: 'How many/much/what ___ do the students in our class ___?' Use visual distributions (dot plots, bar graphs) heavily. Pre-teach: statistical question, variability, distribution, spread. Use multilingual examples from students' experiences.",
            "extending": "Have students differentiate between statistical and non-statistical questions, justifying their reasoning. Ask them to predict distributions before data collection, then compare. Present different distributions and ask 'What does this tell us about variability in the group?'"
        },
        "essential_understandings": [
            "A statistical question anticipates variability in the data—when asked to multiple members of a group, there will be multiple different answers",
            "A distribution shows all the values in a data set along with their frequencies, revealing patterns about what is typical and what is unusual",
            "The spread of a distribution indicates how varied the data is; tight clusters suggest consistency, while spread-out data suggests more variability",
            "Statistical questions require collecting data from a sample and analyzing that data to answer the question about the group"
        ]
    },
    "mean, median, mode, range": {
        "grade": 6,
        "misconceptions": [
            "Students think the mean is always the best representation of the data, not recognizing that outliers can make the mean misleading or that median/mode may better represent the center",
            "Students confuse median with 'middle number' and misorder data or count incorrectly when finding it, especially with even-numbered data sets",
            "Students compute mean correctly but don't understand it as a 'balance point' or what it represents about the data set",
            "Students don't recognize that range describes spread but not clustering—two very different data sets can have the same range"
        ],
        "differentiation": {
            "emergent": "Use physical data: line them up in order and find the middle (median), count frequency of each value (mode), add and divide (mean). Use stacks of counters to show that mean is a 'leveling'—if all stacks were equal height, how tall would each be? Draw range as the distance on a number line.",
            "ell": "Create anchor charts for each measure with pictures and examples. Use consistent language: 'median = middle' (ordered first), 'mode = most often,' 'mean = average (fair share),' 'range = spread.' Pre-teach these terms in both languages. Use bar graphs and line plots heavily.",
            "extending": "Have students collect real data, calculate all four measures, and justify which best describes the data. Present scenarios where mean and median differ significantly; discuss why (outliers). Ask 'What would happen if we added an outlier?' and make predictions before computing."
        },
        "essential_understandings": [
            "Mean (average) is found by summing all values and dividing by the count; it represents a balance point or fair share",
            "Median is the middle value when data is ordered; it divides the data set into two equal halves and is resistant to outliers",
            "Mode is the most frequently occurring value, useful for categorical or repeated data; a data set can be bimodal or have no mode",
            "Range is the difference between the maximum and minimum values, showing spread but not indicating where most values cluster"
        ]
    },
    "proportional relationships": {
        "grade": 7,
        "misconceptions": [
            "Students think if a relationship is proportional, any two quantities that change together are proportional, missing the requirement of a constant ratio",
            "Students believe a proportional relationship must pass through (0,0) on a graph, not recognizing this is a defining characteristic to check when unsure",
            "Students confuse proportional relationships with other types of relationships, such as linear relationships that don't pass through the origin",
            "Students think the constant of proportionality is always a whole number or simple fraction, struggling with values that are decimals"
        ],
        "differentiation": {
            "emergent": "Use tables and graphs from simple, familiar contexts (cost per item, distance at constant speed). Find ratios between corresponding values to identify patterns. Graph ordered pairs and look for straight lines through the origin. Use the 'for every ___' language to build constant ratio understanding.",
            "ell": "Provide sentence frames: 'The ratio of ___ to ___ is always ___.' 'For every ___, there are ___.' Create anchor charts showing tables, graphs, and equations together. Use real-world examples (recipes, unit prices, maps) with bilingual labels. Pre-teach: proportional, constant, ratio, origin.",
            "extending": "Compare proportional and non-proportional relationships in tables and graphs. Have students find the constant of proportionality from a graph (rise/run). Write equations of proportional relationships (y = kx) and explain the meaning of k. Solve word problems requiring identification of proportional relationships."
        },
        "essential_understandings": [
            "A proportional relationship exists when the ratio between two quantities remains constant, expressed as y/x = k (or y = kx)",
            "In a proportional relationship, when one quantity is zero, the other is zero; graphs of proportional relationships are straight lines passing through the origin",
            "The constant of proportionality (k) represents the multiplicative relationship between quantities and can be found from any pair of values",
            "Tables, graphs, equations, and descriptions are different representations of the same proportional relationship"
        ]
    },
    "unit rates and constants of proportionality": {
        "grade": 7,
        "misconceptions": [
            "Students compute a unit rate incorrectly by inverting the fraction or dividing in the wrong order, producing a reciprocal of the actual rate",
            "Students think the unit rate must have 'per 1' in the denominator, not recognizing that unit rates have a denominator of 1 but can be compared differently",
            "Students confuse rate with ratio, not understanding that rates always involve different units (miles per hour) while ratios can have the same units (boys to girls)",
            "Students don't recognize that the constant of proportionality IS the unit rate, treating these as separate concepts"
        ],
        "differentiation": {
            "emergent": "Start with the definition: 'A unit rate tells how much of one quantity per one unit of the other.' Use concrete examples: '12 miles in 3 hours—how many miles in 1 hour?' Show division as distributing equally. Use dimensional analysis (write units and track them).",
            "ell": "Provide sentence frame: '___ per ___' or '___ for every 1 ___.' Create anchor charts showing how to compute unit rates (divide to find 'per 1'). Use consistent notation: 'miles/hour' or 'dollars/pound.' Pre-teach: unit, rate, per, constant.",
            "extending": "Have students find unit rates from tables, graphs, and word problems. Compare unit rates to decide which is a better deal. Recognize that the constant of proportionality IS the unit rate and write equations y = (unit rate) × x."
        },
        "essential_understandings": [
            "A unit rate expresses a ratio where one quantity is 1 (e.g., 60 miles per 1 hour, or simply '60 miles per hour')",
            "Unit rates allow comparison of rates with different quantities by standardizing one quantity to 1",
            "The constant of proportionality in a proportional relationship is the unit rate expressing the relationship between the two quantities",
            "Unit rates are computed by dividing the first quantity by the second, and the order matters (miles per hour is different from hours per mile)"
        ]
    },
    "operations with rational numbers": {
        "grade": 7,
        "misconceptions": [
            "Students think the rules for adding/subtracting integers don't apply to fractions or decimals, treating rational number operations as completely different",
            "Students confuse adding and subtracting negative numbers: '-3 + 5' or '-3 - (-5)', sometimes adding the absolute values instead of considering direction",
            "Students think multiplying always makes numbers bigger and dividing makes them smaller, forgetting this only applies to positive whole numbers",
            "Students don't understand that operations with negative numbers follow the same logic as with positive numbers and zero—they're just extended in the opposite direction"
        ],
        "differentiation": {
            "emergent": "Use number lines and color counters (red/yellow) to model addition and subtraction of negative numbers. Start with integers before fractions or decimals. Build understanding of 'opposites' and 'movement along the number line.' Use real contexts (temperature, debt, elevation).",
            "ell": "Create anchor charts showing operations on number lines with arrows indicating direction. Use consistent language: 'positive,' 'negative,' 'opposite,' 'combine.' Provide sentence frames: 'When we add a negative, we move ___.' Pre-teach vocabulary in both languages with visuals.",
            "extending": "Have students explain why negative times negative equals positive (without just stating the rule). Compare multiplication and division of positive and negative rationals. Present multi-step problems with mixed operations and rational numbers."
        },
        "essential_understandings": [
            "Rational numbers (fractions, decimals, integers) can be added, subtracted, multiplied, and divided using rules that extend from whole number operations",
            "Adding a negative number is the same as subtracting the positive version; subtracting a negative is the same as adding the positive",
            "When multiplying or dividing rational numbers, the signs follow the rule: two positives or two negatives give positive; positive and negative give negative",
            "Operations maintain properties like commutativity, associativity, and distributivity across all rational numbers"
        ]
    },
    "expressions and equivalent forms": {
        "grade": 7,
        "misconceptions": [
            "Students think equivalent expressions must look identical, not recognizing that different arrangements or forms represent the same quantity",
            "Students don't understand the distributive property deeply, applying it mechanically without seeing how it connects to both expanded and factored forms",
            "Students combine unlike terms (e.g., 3x + 2 = 5x), not recognizing that only terms with identical variables and exponents can combine",
            "Students think simplifying always means making an expression shorter, sometimes removing necessary operations"
        ],
        "differentiation": {
            "emergent": "Use area models to show how distributive property works visually (5(2x + 3) = 10x + 15). Build equivalent expressions step-by-step, showing each simplification move. Use algebra tiles or concrete manipulatives to model terms and operations.",
            "ell": "Create anchor charts showing different forms of the same expression: expanded (3x + 3x + 2), partially simplified (6x + 2), and factored (2(3x + 1)). Use color-coding for like terms. Pre-teach: equivalent, simplify, term, factor, distribute.",
            "extending": "Have students create multiple equivalent forms of the same expression and verify by substituting values. Challenge them to move between forms (expand, factor, combine) and explain when each form is most useful. Explore expressions that look different but are equivalent."
        },
        "essential_understandings": [
            "Equivalent expressions represent the same quantity for all values of the variable; they can look different but have identical values",
            "The distributive property connects expanded and factored forms: a(b + c) = ab + ac",
            "Like terms—terms with identical variables and exponents—can be combined by adding or subtracting their coefficients",
            "Simplifying an expression means combining like terms and applying the distributive property, resulting in fewer terms but the same value"
        ]
    },
    "two-step equations and inequalities": {
        "grade": 7,
        "misconceptions": [
            "Students apply operations in the wrong order (not following the reverse order of operations for solving), sometimes dividing before subtracting when they should do the opposite",
            "Students forget to apply the operation to the constant term, losing steps or making algebraic errors",
            "Students don't change the inequality sign when multiplying or dividing by a negative, applying equation rules to inequalities incorrectly",
            "Students solve the equation correctly but can't interpret what the solution means in context, especially for inequalities where a range of values satisfies the condition"
        ],
        "differentiation": {
            "emergent": "Use balance scale models with two-step scenarios. Solve step-by-step aloud: 'First, undo addition/subtraction. Then undo multiplication/division.' Model explicitly on a number line for inequalities (showing shaded region, not just a point).",
            "ell": "Provide step-by-step anchor chart: '1) Undo addition/subtraction first. 2) Undo multiplication/division second. Check your answer.' Use consistent language and visuals. For inequalities: 'Flip the sign when multiplying or dividing by a negative.' Pre-teach solving vocabulary.",
            "extending": "Have students solve two-step equations and justify each step. For inequalities, ask them to identify solutions (all numbers greater than 5) and give examples. Solve word problems requiring two-step equation setup. Compare solutions to equations vs. inequalities visually."
        },
        "essential_understandings": [
            "Two-step equations require undoing operations in reverse order: first subtract/add to isolate the variable term, then multiply/divide to find the variable",
            "The solution to an equation is a single value that makes the statement true; checking by substitution verifies the solution",
            "For inequalities, the solution is typically a range of values (all numbers satisfying the condition); the inequality sign flips when multiplying or dividing by a negative",
            "Inequality solutions can be represented on number lines (with open or closed circles) or described in words (all numbers greater than...)"
        ]
    },
    "scale drawings and scale factor": {
        "grade": 7,
        "misconceptions": [
            "Students think scale factor must be less than 1 (only reductions), not recognizing that enlargements have scale factors greater than 1",
            "Students don't understand that scale factor applies consistently to all linear dimensions (length, width, height), sometimes scaling some dimensions and not others",
            "Students confuse scale factor for lengths (linear) with scale factor for areas, not recognizing that area scale factor is the square of the length scale factor",
            "Students see scale drawings as just 'smaller pictures' without understanding the mathematical relationship: every distance is multiplied by the same factor"
        ],
        "differentiation": {
            "emergent": "Use grid paper to create scale drawings where each grid square represents a unit. Show that if you scale by 2, every dimension multiplies by 2. Draw corresponding dimensions on original and scale drawing, calculating scale factor as a ratio (original/drawing or drawing/original).",
            "ell": "Create anchor chart: 'Scale factor = drawing size / original size' or vice versa. Use sentence frame: 'If the scale factor is 3, every measurement in the drawing is 3 times the actual size.' Pre-teach: scale factor, enlargement, reduction, dimension.",
            "extending": "Have students find scale factor from two drawings or from measurement data. Create scale drawings given dimensions and a scale factor. Explore why area changes by the square of scale factor (if scale factor = 2, area = 4 times as large). Solve map problems using scale."
        },
        "essential_understandings": [
            "A scale factor is the ratio by which all linear dimensions of a figure are multiplied to create a similar figure (scale factor = new size / original size)",
            "Scale factors greater than 1 create enlargements; scale factors between 0 and 1 create reductions; scale factor of 1 creates a congruent figure",
            "All corresponding linear measurements in similar figures have the same scale factor relationship",
            "When linear dimensions are scaled by a factor k, areas are scaled by a factor of k²"
        ]
    },
    "circumference and area of circles": {
        "grade": 7,
        "misconceptions": [
            "Students confuse circumference (perimeter of a circle) with diameter, sometimes adding radius and diameter or using diameter formulas for circumference",
            "Students don't understand what π represents (the ratio of circumference to diameter), treating it as a mysterious magic number to plug in",
            "Students use the wrong radius or diameter when given the other, or use diameter instead of radius (or vice versa) in formulas",
            "Students think the area formula A = πr² requires memorization without understanding that it's related to how many radii fit into the circle"
        ],
        "differentiation": {
            "emergent": "Use physical circles: measure the circumference (string around the edge) and diameter, then calculate their ratio—this IS π. Use circle paper subdivided into sectors to show how area relates to circumference × radius / 2. Build formulas from discovery, not memorization.",
            "ell": "Create anchor chart showing C = πd or C = 2πr with pictures and measurements labeled. Show A = πr² similarly. Use multilingual measurement tools and vocabulary: circumference, diameter, radius, area. Pre-teach and show visual examples.",
            "extending": "Have students derive the area formula by dividing a circle into many sectors and rearranging into a parallelogram (A = base × height = πr × r = πr²). Compare circles with different radii and predict area changes. Solve problems involving both circumference and area."
        },
        "essential_understandings": [
            "The circumference of a circle (distance around) is related to its diameter by the constant π: C = πd or C = 2πr",
            "Pi (π) is the ratio of circumference to diameter (approximately 3.14159...) and appears in all circle formulas",
            "The area of a circle is A = πr², which can be understood by dividing the circle into sectors and rearranging them into a parallelogram",
            "Both circumference and area depend on the radius: doubling the radius doubles the circumference but quadruples the area"
        ]
    },
    "angle relationships": {
        "grade": 7,
        "misconceptions": [
            "Students think complementary angles must be adjacent, not recognizing that complementary means the measures sum to 90° regardless of position",
            "Students confuse supplementary (sum to 180°) with complementary (sum to 90°), sometimes flipping the definitions",
            "Students believe vertical angles are always equal without understanding the reasoning (angles formed by intersecting lines), treating it as a mere rule",
            "Students don't recognize angle relationships in geometric figures (triangles, parallel lines cut by transversals), missing opportunities to find missing angle measures"
        ],
        "differentiation": {
            "emergent": "Use angle manipulatives and tools to physically show complementary (90°) and supplementary (180°) angles. Draw pairs of lines and label all four angles formed by intersection, identifying vertical angles and their equal measures. Use visual angle cards.",
            "ell": "Create multilingual anchor chart showing each angle relationship with pictures: complementary (two angles making a right angle), supplementary (two angles making a straight line), vertical (opposite angles at intersection). Use consistent language and colors. Pre-teach vocabulary.",
            "extending": "Identify all angle relationships in parallel lines cut by transversals (corresponding, alternate interior, etc.). Find missing angles in complex geometric figures using multiple relationships. Explain why vertical angles must be equal using angle relationships and properties of straight lines."
        },
        "essential_understandings": [
            "Complementary angles are two angles whose measures sum to 90°; supplementary angles are two angles whose measures sum to 180°",
            "Vertical angles (opposite angles formed by two intersecting lines) are always congruent (equal in measure)",
            "When two parallel lines are cut by a transversal, corresponding angles are congruent and alternate interior angles are congruent",
            "Angle relationships can be used to find missing angle measures in geometric figures and in real-world applications"
        ]
    },
    "probability (theoretical, experimental, compound)": {
        "grade": 7,
        "misconceptions": [
            "Students think theoretical and experimental probability must be equal or that experimental probability will match theory after just a few trials, not understanding the law of large numbers",
            "Students believe past results affect future outcomes in independent events ('the coin is due for heads'), confusing dependent and independent events",
            "Students think compound probability is just adding individual probabilities, not recognizing that the type of compound event (and/or) and whether events are independent matters",
            "Students confuse 'likely' and 'certain' and don't understand that probability values must be between 0 and 1 (or 0% and 100%)"
        ],
        "differentiation": {
            "emergent": "Conduct experiments: flip coins, roll dice, draw from bags. Record results and calculate experimental probability (successful outcomes / total trials). Compare to theoretical probability. Do this many times to show how experimental approaches theoretical with more trials.",
            "ell": "Create anchor chart: 'Theoretical probability = possible outcomes / total outcomes.' 'Experimental probability = actual outcomes / trials conducted.' Use sentence frames: 'There are ___ ways to get ___.' 'The probability is ___.' Pre-teach: probability, outcome, theoretical, experimental.",
            "extending": "Have students predict experimental probability results, conduct trials, and compare. Explore compound events: 'What's the probability of rolling a 2 AND flipping heads?' Use tree diagrams or area models to show all possibilities. Compare independent and dependent events."
        },
        "essential_understandings": [
            "Theoretical probability is calculated from the possible outcomes (probability = favorable outcomes / total possible outcomes)",
            "Experimental probability is determined by conducting trials and recording actual results (probability = actual successful outcomes / total trials)",
            "As the number of trials increases, experimental probability approaches theoretical probability (law of large numbers)",
            "For compound events, if events are independent, multiply their individual probabilities; for dependent events or 'or' events, the calculation differs based on whether outcomes overlap"
        ]
    },
    "random sampling and inferences": {
        "grade": 7,
        "misconceptions": [
            "Students don't understand why random sampling matters, thinking that any sample is representative of the population, even if it's biased",
            "Students confuse population (the entire group) with sample (the subset studied), sometimes treating sample statistics as the only correct answer",
            "Students think inferences must be certain and exact, not recognizing that inferences are generalizations with uncertainty that depends on sample quality",
            "Students don't recognize sampling bias, missing how non-random selection methods (volunteers, convenience samples) skew results"
        ],
        "differentiation": {
            "emergent": "Use physical demonstration: fill a bag with beads (population), draw randomly (sample), and estimate the proportion in the population. Repeat with biased sampling (always picking from one side) to show how bias affects inferences. Use familiar context (surveying class about preferences).",
            "ell": "Create anchor chart: 'Population = all people/objects.' 'Sample = the group we study.' 'Random = every member has equal chance.' 'Bias = unfair selection method.' Use sentence frames: 'We sampled ___ out of the population of ___.' 'We can infer that ___.' Pre-teach vocabulary.",
            "extending": "Have students plan surveys for different questions, deciding on population and sample size. Identify potential biases in given survey methods. Use sample data to make inferences and estimate population proportions. Discuss confidence and margin of error informally."
        },
        "essential_understandings": [
            "A random sample is one where every member of the population has an equal chance of being selected, making it likely to be representative",
            "Inferences about a population are generalizations based on sample data; the quality of inferences depends on sample quality and size",
            "Bias in sampling (when some members are more likely to be chosen) can lead to inferences that misrepresent the population",
            "Larger, randomly selected samples generally lead to more reliable inferences than small or biased samples"
        ]
    },
    "exponents and scientific notation": {
        "grade": 8,
        "misconceptions": [
            "Students think exponents mean multiplication (2³ = 2 × 3) rather than repeated multiplication (2 × 2 × 2), confusing them with multiplication coefficients",
            "Students think any large number can be written in scientific notation, not recognizing the requirement that the coefficient must be between 1 and 10",
            "Students believe that raising a number to a power always makes it bigger, missing that 0 < base < 1 raised to a power gives a smaller result",
            "Students don't understand that scientific notation uses powers of 10 to show place value, missing the connection between exponents and decimal place movement"
        ],
        "differentiation": {
            "emergent": "Build exponents with repeated multiplication: 2³ = 2 × 2 × 2. Use area and volume models (2² is a square, 2³ is a cube). Introduce scientific notation as a way to write large numbers by counting place values: 5,000 = 5 × 10³.",
            "ell": "Create anchor chart showing exponential form, expanded form, and standard form side-by-side. Use sentence frames: '2 to the power of 3 equals ___.' 'In scientific notation, ___ is written as ___.' Pre-teach: exponent, base, power, scientific notation.",
            "extending": "Explore negative exponents and why 10⁻² = 0.01 (using patterns in powers of 10). Convert between scientific notation and standard form. Compare numbers in scientific notation. Apply to real data (distances, populations, very small measures)."
        },
        "essential_understandings": [
            "An exponent indicates how many times the base is multiplied by itself; aⁿ = a × a × ... × a (n times)",
            "Powers of 10 show place value and decimal position: 10³ = 1,000 (three places), 10⁻³ = 0.001 (three decimal places)",
            "Scientific notation expresses numbers as a × 10ⁿ where 1 ≤ a < 10 and n is an integer, useful for very large or very small numbers",
            "Laws of exponents (product rule, quotient rule, power rule) simplify operations with exponents"
        ]
    },
    "square roots and irrational numbers": {
        "grade": 8,
        "misconceptions": [
            "Students think √9 = 3 or -3 (including the negative), not recognizing that the principal square root is the non-negative value",
            "Students believe all numbers can be expressed as fractions, not understanding that irrational numbers like √2 and π cannot be written as a ratio of integers",
            "Students think √(a + b) = √a + √b, applying distribution to radicals incorrectly without checking with simple examples",
            "Students don't understand where irrational numbers 'fit' on the number line, sometimes thinking they're not 'real' or can't be approximated"
        ],
        "differentiation": {
            "emergent": "Use area models: √9 is the side length of a square with area 9. Show that √2 is between 1 and 2 by finding area squares. Use number lines to place approximate values (√2 ≈ 1.4). Build understanding of square roots as 'opposite' of squaring.",
            "ell": "Create anchor chart: 'A square root is the opposite of squaring.' '√9 = 3 because 3² = 9.' 'Some square roots are irrational (can't be written as fractions).' Show √2 ≈ 1.414... on a number line. Pre-teach: square root, irrational, approximate, principal.",
            "extending": "Have students locate irrational numbers on number lines between integers. Simplify radicals by factoring (√12 = 2√3). Explore why certain numbers are rational and others irrational. Present real-world contexts where irrational numbers appear (diagonal of unit square = √2)."
        },
        "essential_understandings": [
            "A square root of a number is a value that, when multiplied by itself, equals the original number; the principal square root is the non-negative root",
            "Perfect squares have rational square roots; non-perfect squares have irrational square roots that cannot be expressed as fractions",
            "Irrational numbers exist on the number line and can be approximated as decimals; examples include √2, √3, and π",
            "The square root of a number between 0 and 1 is larger than the original (e.g., √0.25 = 0.5), while square roots of numbers greater than 1 are smaller than the original"
        ]
    },
    "linear functions and slope": {
        "grade": 8,
        "misconceptions": [
            "Students think slope is the same as y-intercept or don't recognize that slope describes steepness (rate of change) while y-intercept is the starting value",
            "Students calculate slope as run/rise (inverted), or use (x₂ - x₁)/(y₂ - y₁) instead of (y₂ - y₁)/(x₂ - x₁)",
            "Students believe slope must be a whole number or simple fraction, struggling with undefined slopes (vertical lines) or zero slope (horizontal lines)",
            "Students don't connect slope to real-world rate of change (speed, cost per item), seeing it as an abstract mathematical concept"
        ],
        "differentiation": {
            "emergent": "Use physical slopes (ramps, inclined planes) and measure rise/run. Plot points on grids and count rise and run. Use movement language: 'Rise first (vertical), then run (horizontal).' Connect to real contexts: climb 3 units, move 2 units over = slope of 3/2.",
            "ell": "Create anchor chart: 'Slope = rise / run = (y₂ - y₁) / (x₂ - x₁).' Use sentence frames: 'The slope is ___. This means for every ___ units horizontal, we go ___ units vertical.' Pre-teach: slope, rise, run, steep, y-intercept.",
            "extending": "Have students find slope from graphs, tables, and two points. Explore why slope is constant on a line. Connect to linear equations (y = mx + b where m is slope). Solve real-world problems where slope represents rate of change."
        },
        "essential_understandings": [
            "Slope is the ratio of vertical change (rise) to horizontal change (run) between any two points on a line, representing rate of change",
            "For a line through points (x₁, y₁) and (x₂, y₂), slope = (y₂ - y₁) / (x₂ - x₁); positive slope goes up right, negative slope goes down right",
            "A line has constant slope; this constant rate of change is a defining property of linear functions",
            "In the equation y = mx + b, m is the slope (rate of change) and b is the y-intercept (starting value)"
        ]
    },
    "systems of linear equations": {
        "grade": 8,
        "misconceptions": [
            "Students think a system of equations has multiple solutions when in fact most systems have exactly one solution (or no solution, or infinitely many if equations are equivalent)",
            "Students use substitution or elimination but make algebraic errors, like failing to distribute or losing a term in the process",
            "Students don't check whether their solution satisfies both equations, accepting an answer that works for only one",
            "Students don't recognize when a system has no solution (parallel lines) or infinitely many solutions (same line), treating it as an error rather than a valid outcome"
        ],
        "differentiation": {
            "emergent": "Use graphing to solve systems—where the lines intersect is the solution. Use concrete examples: 'One class has x students, another has y students, and together they have 30. Here's another constraint...' Solve by graphing before introducing algebraic methods.",
            "ell": "Create anchor charts for substitution and elimination methods with step-by-step examples. Use consistent language: 'intersection point,' 'solution,' 'check.' Provide sentence frames: 'The solution is the point where ___.' 'We check by substituting ___.' Pre-teach methods in both languages.",
            "extending": "Have students solve the same system using different methods (graphing, substitution, elimination) and verify results match. Create a system with no solution or infinitely many solutions and explain graphically why. Apply to real-world contexts (break-even points, fair pricing)."
        },
        "essential_understandings": [
            "A system of linear equations is a set of equations with the same variables; the solution is an ordered pair (or set of pairs) satisfying all equations simultaneously",
            "Graphically, the solution is the intersection point(s) of the lines; algebraically, substitution and elimination methods find these solutions",
            "A system can have exactly one solution (lines intersect at one point), no solution (parallel lines), or infinitely many solutions (same line)",
            "Solutions must be checked by substituting back into all original equations"
        ]
    },
    "solving multi-step equations": {
        "grade": 8,
        "misconceptions": [
            "Students don't apply the distributive property correctly before combining like terms, making algebraic errors early in the process",
            "Students forget to apply operations to all terms on both sides, not maintaining equality throughout the solving process",
            "Students combine unlike terms, treating all variables the same regardless of whether they're the same variable with the same exponent",
            "Students solve the equation correctly but then make errors interpreting or checking the solution against the original equation"
        ],
        "differentiation": {
            "emergent": "Model solving with algebra tiles: build the equation, remove tiles equally from both sides. Verbalize each step aloud. Start with simpler equations (2x + 3 = 7) before moving to those with variables on both sides or distribution needed.",
            "ell": "Create detailed anchor chart showing each step of solving a multi-step equation: 'Step 1: Distribute. Step 2: Combine like terms. Step 3: Get variable on one side. Step 4: Undo addition/subtraction. Step 5: Undo multiplication/division. Step 6: Check.' Use consistent formatting and visuals.",
            "extending": "Have students solve equations with variables on both sides. Equations requiring distribution and combining like terms. Equations with rational number coefficients. Ask them to explain why each step is necessary and verify solutions."
        },
        "essential_understandings": [
            "Multi-step equations require systematically undoing operations in reverse order: distribution, combining like terms, moving variable terms to one side, undoing addition/subtraction, undoing multiplication/division",
            "The distributive property must be applied before attempting to combine like terms or move variables",
            "Only terms with identical variables and exponents can be combined; unlike terms remain separate",
            "The solution must be checked by substituting back into the original equation to verify equality"
        ]
    },
    "pythagorean theorem": {
        "grade": 8,
        "misconceptions": [
            "Students memorize a² + b² = c² without understanding that c must be the hypotenuse (side opposite the right angle), applying it to any triangle",
            "Students think the Pythagorean theorem applies to all triangles, not recognizing it's specific to right triangles",
            "Students incorrectly identify which sides are legs and which is hypotenuse, leading to wrong answers even if the computation is correct",
            "Students don't connect the theorem to real contexts or don't recognize when a situation requires its application"
        ],
        "differentiation": {
            "emergent": "Use physical squares cut from grid paper: build squares on each side of right triangles and show that the two smaller squares' areas equal the largest square's area. Start with familiar Pythagorean triples (3-4-5, 5-12-13) before introducing square roots.",
            "ell": "Create anchor chart showing a right triangle with legs labeled a and b, hypotenuse labeled c, and the equation a² + b² = c². Use consistent language: 'legs' (sides forming the right angle), 'hypotenuse' (longest side). Pre-teach vocabulary with visuals.",
            "extending": "Have students verify Pythagorean triples and find others. Use the theorem to find missing side lengths in right triangles. Determine whether a triangle is a right triangle given three side lengths. Apply to real contexts (ladder distance from wall, diagonal of a room)."
        },
        "essential_understandings": [
            "In a right triangle, the sum of the squares of the two legs equals the square of the hypotenuse: a² + b² = c²",
            "The hypotenuse is the longest side in a right triangle, opposite the right angle; the legs are the two sides forming the right angle",
            "The Pythagorean theorem can be used to find a missing side length if two sides are known, or to verify whether a triangle is a right triangle",
            "The theorem applies only to right triangles and is a fundamental relationship in geometry and trigonometry"
        ]
    },
    "transformations": {
        "grade": 8,
        "misconceptions": [
            "Students think transformations change the size or shape of a figure, not recognizing that translations, reflections, and rotations preserve both (only dilations change size)",
            "Students don't understand the difference between rigid transformations (preserve size and shape) and non-rigid transformations (dilations, which preserve shape but not size)",
            "Students apply transformations incorrectly (e.g., reflecting across the wrong line, rotating the wrong direction), showing misunderstanding of the transformation rule",
            "Students don't recognize when figures are related by transformations, missing correspondences and properties of congruence"
        ],
        "differentiation": {
            "emergent": "Use physical manipulatives: trace a shape, slide it (translation), flip it (reflection), turn it (rotation). Observe that the shape stays the same size and shape. Use coordinate grids to show translations and dilations. Mark and label vertices before and after.",
            "ell": "Create anchor chart for each transformation type with examples: translation (slide), reflection (flip), rotation (turn), dilation (enlarge/shrink). Use visuals and consistent language. Pre-teach vocabulary in both languages. Show how vertices move with each transformation.",
            "extending": "Have students apply multiple transformations in sequence and describe the overall effect. Identify transformations from before-and-after figures. Explore rotation angles and reflection lines. Use dilations to enlarge/shrink and maintain proportions."
        },
        "essential_understandings": [
            "A translation (slide) moves a figure in a straight line without changing its size, shape, or orientation",
            "A reflection (flip) creates a mirror image across a line; the figure maintains size and shape, but orientation reverses",
            "A rotation (turn) moves a figure around a point by an angle; size and shape are preserved but orientation changes",
            "A dilation enlarges or shrinks a figure while preserving shape (all angles stay the same, sides remain proportional); dilations are non-rigid transformations"
        ]
    },
    "congruence and similarity": {
        "grade": 8,
        "misconceptions": [
            "Students confuse congruence (same size and shape) with similarity (same shape, different size), sometimes treating them as the same concept",
            "Students think figures are congruent if they have matching angles or matching sides, not recognizing that congruence requires all angles AND sides to match",
            "Students don't recognize corresponding parts of congruent or similar figures, making errors when setting up proportions or identifying equal angles",
            "Students think similarity requires exact same proportions, missing that figures with matching angles are similar regardless of side length differences"
        ],
        "differentiation": {
            "emergent": "Use physical models: two identical shapes are congruent; same shape in two sizes are similar. Mark and color corresponding vertices and sides. Show that congruent figures fit perfectly on top of each other; similar figures don't, but angles match.",
            "ell": "Create anchor chart comparing congruence and similarity with examples. Use color-coding for corresponding parts. Sentence frames: 'These figures are congruent because ___.' 'These figures are similar because ___.' Pre-teach: congruent, similar, corresponding, proportional.",
            "extending": "Have students identify corresponding parts in congruent and similar figures, setting up proportions for sides in similar figures. Determine scale factor between similar figures. Use congruence statements with proper correspondence (triangle ABC is congruent to triangle DEF)."
        },
        "essential_understandings": [
            "Congruent figures have the same size and shape; all corresponding angles are equal and all corresponding sides are equal in length",
            "Similar figures have the same shape but different sizes; all corresponding angles are equal and all corresponding sides are proportional",
            "Transformations (translations, reflections, rotations) create congruent figures; dilations followed by rigid transformations create similar figures",
            "Corresponding angles in similar figures are congruent, and corresponding sides are proportional with a constant ratio (scale factor)"
        ]
    },
    "volume of cylinders, cones, spheres": {
        "grade": 8,
        "misconceptions": [
            "Students confuse volume of cylinders (πr²h) with surface area, or apply formulas for one shape to another without justifying why",
            "Students think the volume of a cone is the same as the volume of a cylinder with the same base and height, missing the 1/3 factor",
            "Students believe volume formulas for 3D shapes are unrelated, not recognizing how cones and spheres relate to cylinders (cone = 1/3 cylinder, sphere = 4/3 times certain cylinder)",
            "Students compute correctly but use wrong units (cubic centimeters instead of square units, or missing units entirely)"
        ],
        "differentiation": {
            "emergent": "Use physical cylinders, cones, and spheres filled with water or sand to demonstrate relative volumes: a cone holds 1/3 what a cylinder holds. Build understanding from concrete experiences, then move to formulas.",
            "ell": "Create anchor chart for each shape showing formula with a picture, labeling r (radius) and h (height). Use sentence frames: 'The volume of a cylinder is ___.' 'A cone holds 1/3 the volume of a ___.' Pre-teach: cylinder, cone, sphere, base, height.",
            "extending": "Have students derive why cone volume is 1/3 cylinder volume using the physical relationship. Solve real-world problems (tank capacity, ice cream cones, ball dimensions). Compare volumes when dimensions change proportionally."
        },
        "essential_understandings": [
            "The volume of a cylinder is V = πr²h (base area times height); the base is a circle with area πr²",
            "The volume of a cone is V = (1/3)πr²h—exactly 1/3 the volume of a cylinder with the same base and height",
            "The volume of a sphere is V = (4/3)πr³, which can be understood as 4/3 times the volume of a cylinder when viewed in a certain way",
            "Volume formulas are measured in cubic units; understanding the relationships between these shapes helps remember and justify formulas"
        ]
    },
    "scatter plots and trend lines": {
        "grade": 8,
        "misconceptions": [
            "Students think every scatter plot shows a linear relationship, not recognizing nonlinear or no relationship scenarios",
            "Students draw trend lines through every point rather than finding a line that shows the general pattern and trend of the data",
            "Students don't understand what a trend line represents (best approximation of the relationship), sometimes confusing it with a line of best fit calculation",
            "Students make predictions using trend lines without considering whether extrapolation beyond the data range is reasonable"
        ],
        "differentiation": {
            "emergent": "Plot familiar data (height vs. shoe size, study time vs. test score) on scatter plots. Visually find the general direction (positive/negative slope, or no relationship). Draw a line showing the trend, not necessarily through points. Use 'eyeballing' before formal methods.",
            "ell": "Create anchor chart showing various scatter plots (positive relationship, negative, no relationship) with descriptive language. Teach: 'A trend line shows the pattern.' Use sentence frames: 'As ___ increases, ___ ___.' Pre-teach vocabulary with visuals.",
            "extending": "Have students find the trend line using slope of two representative points. Make and justify predictions using the trend line. Analyze data clusters and outliers. Discuss when trend lines are appropriate and when data suggests other relationships."
        },
        "essential_understandings": [
            "A scatter plot shows the relationship between two variables; each point represents one data pair",
            "The relationship between variables can be positive (both increase), negative (one increases, one decreases), or show no clear pattern",
            "A trend line is a straight line that approximates the overall pattern in a scatter plot, useful for making predictions",
            "Trend lines should follow the general flow of data rather than passing through specific points; predictions using trend lines are estimates that depend on data quality"
        ]
    },
    "two-way frequency tables": {
        "grade": 8,
        "misconceptions": [
            "Students don't understand how to read two-way frequency tables, confusing row totals with column totals or missing the relationships between categories",
            "Students calculate relative frequency incorrectly (using total instead of row/column total), not recognizing the difference between conditional and unconditional frequency",
            "Students can't interpret the table or use it to make comparisons, seeing it as just numbers without meaning",
            "Students don't recognize how to use two-way tables to determine if variables are independent or if associations exist"
        ],
        "differentiation": {
            "emergent": "Start with simple tables (2×2) about familiar topics (lunch preferences by grade level). Read specific cells aloud and discuss their meanings. Calculate row and column totals visually. Move to interpretation: 'Out of boys, how many prefer pizza?'",
            "ell": "Create annotated anchor chart showing a completed two-way table with highlighted row totals, column totals, grand total, and specific cells. Use sentence frames: 'The table shows ___.' 'The total number of ___ is ___.' Pre-teach: row, column, frequency, total.",
            "extending": "Have students construct their own two-way frequency tables from data. Calculate conditional relative frequencies ('Of all students who chose sushi, what percentage are in grade 7?'). Compare conditional frequencies to determine associations. Interpret relationships in context."
        },
        "essential_understandings": [
            "A two-way frequency table displays the frequency of categorical data organized by two variables, showing counts in rows and columns",
            "Row and column totals provide marginal frequencies (totals for each category); individual cells show joint frequencies (counts for combinations)",
            "Conditional relative frequency answers 'What percentage of one group chose X?' by dividing a specific count by its row or column total",
            "Two-way frequency tables reveal whether variables are independent (similar distributions across categories) or associated (different distributions)"
        ]
    }
}
RISA_DIALOGUES_COMPLETE = {
    "ratios and rates": {
        "grade": 6,
        "social": {
            "title": "Talking About Ratios",
            "vocabulary": ["ratio", "rate", "comparison", "for every", "recipe"],
            "script": [
                {"speaker": "A", "line": "Hi! Do you like to cook?"},
                {"speaker": "B", "line": "Yes, I do! I made cookies last week."},
                {"speaker": "A", "line": "Nice! In a recipe, if you need 2 cups of flour for every 1 cup of sugar, what does that mean?"},
                {"speaker": "B", "line": "It means I need _____ more flour than sugar."},
                {"speaker": "A", "line": "Right! That's a ratio. If you doubled the recipe, you would need _____ cups of flour and _____ cup of sugar."},
                {"speaker": "B", "line": "Oh! So the ratio stays the same, but the amounts get _____?"},
                {"speaker": "A", "line": "Exactly! You really understand ratios. That's great!"},
                {"speaker": "B", "line": "Thanks for helping me see it!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Ratios and Rates",
            "vocabulary": ["ratio", "rate", "unit rate", "equivalent ratios", "proportion", "scale"],
            "script": [
                {"speaker": "A", "line": "Good morning. I'd like to discuss ratios with you."},
                {"speaker": "B", "line": "I am ready. What would you like to know?"},
                {"speaker": "A", "line": "A ratio of 3:5 compares two quantities. Can you give me an example of a situation where we might use this ratio?"},
                {"speaker": "B", "line": "A ratio of 3:5 could mean _____ for every _____ of something else."},
                {"speaker": "A", "line": "Good. Now, how would you find the unit rate if you have a ratio of 120 miles to 3 hours?"},
                {"speaker": "B", "line": "I would divide _____ by _____ to get _____ miles per hour."},
                {"speaker": "A", "line": "Precisely. Why are unit rates useful when comparing rates?"},
                {"speaker": "B", "line": "They help us _____ different rates on the same scale so we can see which is faster or better."},
                {"speaker": "A", "line": "Excellent reasoning. You understand rates and unit rates very well."},
                {"speaker": "B", "line": "Thank you for this discussion."}
            ]
        }
    },
    "division of fractions": {
        "grade": 6,
        "social": {
            "title": "Sharing and Fractions",
            "vocabulary": ["fraction", "divide", "share", "equal parts", "reciprocal"],
            "script": [
                {"speaker": "A", "line": "Hey! Do you have any pizza?"},
                {"speaker": "B", "line": "I have half a pizza. What about you?"},
                {"speaker": "A", "line": "I want to share it with 2 friends. If you divide 1/2 pizza by 2, how much does each person get?"},
                {"speaker": "B", "line": "Each person gets _____ of the pizza."},
                {"speaker": "A", "line": "Right! So 1/2 ÷ 2 = _____. What if you divide 3/4 by 1/2?"},
                {"speaker": "B", "line": "Hmm, I think that's _____."},
                {"speaker": "A", "line": "You're thinking about it the right way! I'm proud of you."},
                {"speaker": "B", "line": "Thanks! Now I get it!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Division of Fractions",
            "vocabulary": ["dividend", "divisor", "reciprocal", "multiplicative inverse", "equivalent fractions"],
            "script": [
                {"speaker": "A", "line": "Good morning. Shall we discuss fraction division?"},
                {"speaker": "B", "line": "Yes, I would appreciate that."},
                {"speaker": "A", "line": "When we divide 3/4 by 1/2, what operation do we actually perform?"},
                {"speaker": "B", "line": "We multiply 3/4 by the _____ of 1/2, which is _____."},
                {"speaker": "A", "line": "Correct. Why do we multiply by the reciprocal instead of dividing directly?"},
                {"speaker": "B", "line": "Because dividing by a fraction is the same as _____ by its reciprocal."},
                {"speaker": "A", "line": "Excellent. Now, what is 5/6 ÷ 3/4?"},
                {"speaker": "B", "line": "That is 5/6 times 4/3, which equals _____."},
                {"speaker": "A", "line": "Very good. You have mastered fraction division."},
                {"speaker": "B", "line": "Thank you for your clear explanations."}
            ]
        }
    },
    "positive and negative numbers": {
        "grade": 6,
        "social": {
            "title": "Hot and Cold, Positive and Negative",
            "vocabulary": ["positive", "negative", "temperature", "above zero", "below zero", "opposite"],
            "script": [
                {"speaker": "A", "line": "It's really cold today! It's 5 degrees below zero."},
                {"speaker": "B", "line": "Yes! We write that as _____5 degrees."},
                {"speaker": "A", "line": "Right! And if it's 10 degrees above zero, we write it as _____?"},
                {"speaker": "B", "line": "We write it as +10 or just 10 degrees."},
                {"speaker": "A", "line": "Good! What is the opposite of 3?"},
                {"speaker": "B", "line": "The opposite of 3 is _____, because they're the same distance from zero."},
                {"speaker": "A", "line": "Perfect! You understand positive and negative numbers!"},
                {"speaker": "B", "line": "Thanks for showing me!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Positive and Negative Numbers",
            "vocabulary": ["integers", "additive inverse", "absolute value", "number line", "directed quantities"],
            "script": [
                {"speaker": "A", "line": "Good morning. I would like to explore integers with you."},
                {"speaker": "B", "line": "I am prepared. Please proceed."},
                {"speaker": "A", "line": "What is the additive inverse of -7?"},
                {"speaker": "B", "line": "The additive inverse of -7 is _____, because their sum equals _____."},
                {"speaker": "A", "line": "Correct. Why is the concept of additive inverse important in mathematics?"},
                {"speaker": "B", "line": "Because it helps us _____ negative numbers and solve equations."},
                {"speaker": "A", "line": "Indeed. If a point on a number line is at -15, what is its distance from zero?"},
                {"speaker": "B", "line": "The distance is _____ units, which we call the absolute value of -15."},
                {"speaker": "A", "line": "Excellent understanding. You are ready to work with integer operations."},
                {"speaker": "B", "line": "I appreciate this thorough discussion."}
            ]
        }
    },
    "absolute value": {
        "grade": 6,
        "social": {
            "title": "Distance from Zero",
            "vocabulary": ["absolute value", "distance", "zero", "number line", "symbol |"],
            "script": [
                {"speaker": "A", "line": "Do you know what absolute value means?"},
                {"speaker": "B", "line": "I think it has something to do with distance?"},
                {"speaker": "A", "line": "Yes! It's how far a number is from zero. What is |5|?"},
                {"speaker": "B", "line": "It's _____ because 5 is _____ units away from zero."},
                {"speaker": "A", "line": "Right! And what about |-5|?"},
                {"speaker": "B", "line": "That's also _____, because -5 is also _____ units from zero."},
                {"speaker": "A", "line": "Exactly! Both 5 and -5 have the same absolute value."},
                {"speaker": "B", "line": "Oh, I get it now! That makes sense!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Absolute Value",
            "vocabulary": ["absolute value", "distance", "magnitude", "non-negative", "real number line"],
            "script": [
                {"speaker": "A", "line": "Good afternoon. Let us discuss absolute value."},
                {"speaker": "B", "line": "I would be pleased to learn more."},
                {"speaker": "A", "line": "Absolute value measures the _____ of a number from zero on the number line."},
                {"speaker": "B", "line": "So |−8| = _____ and |8| = _____, correct?"},
                {"speaker": "A", "line": "Precisely. Why is absolute value always non-negative?"},
                {"speaker": "B", "line": "Because distance is always _____ and cannot be negative."},
                {"speaker": "A", "line": "Well stated. Now, what is |−3 + 5|?"},
                {"speaker": "B", "line": "First, I simplify: −3 + 5 = _____, then |2| = _____."},
                {"speaker": "A", "line": "Excellent. You understand absolute value and its properties thoroughly."},
                {"speaker": "B", "line": "Your guidance has been most helpful."}
            ]
        }
    },
    "variables and expressions": {
        "grade": 6,
        "social": {
            "title": "Mystery Numbers and Letters",
            "vocabulary": ["variable", "expression", "unknown", "letter", "substitute"],
            "script": [
                {"speaker": "A", "line": "I'm thinking of a mystery number."},
                {"speaker": "B", "line": "Can you give me a clue?"},
                {"speaker": "A", "line": "Sure! If I call it x, and I add 5 to it, I get 12. What is x?"},
                {"speaker": "B", "line": "So x = _____?"},
                {"speaker": "A", "line": "Yes! Now, can you write an expression that means 'three times my mystery number'?"},
                {"speaker": "B", "line": "That would be _____ or 3x."},
                {"speaker": "A", "line": "Perfect! You're really good at this!"},
                {"speaker": "B", "line": "Thanks! Variables are easier now!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Variables and Expressions",
            "vocabulary": ["variable", "algebraic expression", "term", "coefficient", "constant"],
            "script": [
                {"speaker": "A", "line": "Hello. Today I want to explore algebraic expressions."},
                {"speaker": "B", "line": "I am ready. What should we examine?"},
                {"speaker": "A", "line": "In the expression 4x + 7, what does x represent?"},
                {"speaker": "B", "line": "The variable x represents an _____ value that we don't yet know."},
                {"speaker": "A", "line": "Correct. What is the coefficient, and what does it mean?"},
                {"speaker": "B", "line": "The coefficient is _____, which means we multiply x by _____."},
                {"speaker": "A", "line": "Good. Now, if x = 3, what is the value of 4x + 7?"},
                {"speaker": "B", "line": "I substitute: 4(3) + 7 = _____ + 7 = _____."},
                {"speaker": "A", "line": "Excellent work. You understand variables and expression evaluation."},
                {"speaker": "B", "line": "Thank you for this instructive lesson."}
            ]
        }
    },
    "one-step equations": {
        "grade": 6,
        "social": {
            "title": "Finding the Mystery Number",
            "vocabulary": ["equation", "equal", "solve", "operation", "balance"],
            "script": [
                {"speaker": "A", "line": "I have an equation: x + 4 = 9. Can you solve it?"},
                {"speaker": "B", "line": "What does that mean?"},
                {"speaker": "A", "line": "It means some number plus 4 equals 9. What is that number?"},
                {"speaker": "B", "line": "If I subtract 4 from both sides, x = _____?"},
                {"speaker": "A", "line": "Yes! Now solve 3y = 15 for y."},
                {"speaker": "B", "line": "I divide both sides by 3, so y = _____."},
                {"speaker": "A", "line": "That's exactly right! You solved it!"},
                {"speaker": "B", "line": "Great! That was actually fun!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: One-Step Equations",
            "vocabulary": ["equation", "solution", "inverse operation", "additive inverse", "multiplicative inverse"],
            "script": [
                {"speaker": "A", "line": "Good morning. Let us solve one-step equations."},
                {"speaker": "B", "line": "I am prepared to begin."},
                {"speaker": "A", "line": "To solve x - 8 = 12, what inverse operation must we use?"},
                {"speaker": "B", "line": "We use the _____ operation, which is _____, to isolate x."},
                {"speaker": "A", "line": "Correct. Solve for x."},
                {"speaker": "B", "line": "x - 8 + 8 = 12 + 8, so x = _____."},
                {"speaker": "A", "line": "Good. Now solve 5z = 35 and explain your reasoning."},
                {"speaker": "B", "line": "Since z is multiplied by 5, I divide both sides by 5: z = _____."},
                {"speaker": "A", "line": "Perfect. You understand inverse operations and solution verification."},
                {"speaker": "B", "line": "This has been a valuable lesson."}
            ]
        }
    },
    "area of polygons": {
        "grade": 6,
        "social": {
            "title": "Measuring Space Inside Shapes",
            "vocabulary": ["area", "polygon", "square units", "length", "width", "base", "height"],
            "script": [
                {"speaker": "A", "line": "Do you know how to find the area of a rectangle?"},
                {"speaker": "B", "line": "I think you multiply something?"},
                {"speaker": "A", "line": "Yes! You multiply length times width. If a rectangle is 5 units long and 3 units wide, what's the area?"},
                {"speaker": "B", "line": "The area is _____ square units."},
                {"speaker": "A", "line": "Great! Now, for a triangle with the same base and height, is the area bigger or smaller?"},
                {"speaker": "B", "line": "A triangle is smaller because the formula is _____ times base times height."},
                {"speaker": "A", "line": "Excellent! You understand area formulas!"},
                {"speaker": "B", "line": "Thanks for breaking it down!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Area of Polygons",
            "vocabulary": ["area", "polygon", "square units", "base", "height", "altitude", "formula"],
            "script": [
                {"speaker": "A", "line": "Good morning. Today we will calculate areas of polygons."},
                {"speaker": "B", "line": "I am ready to learn."},
                {"speaker": "A", "line": "The area of a rectangle is calculated as length times width. What are the units?"},
                {"speaker": "B", "line": "The units are _____, such as square centimeters or square meters."},
                {"speaker": "A", "line": "Correct. Now, for a parallelogram, which dimension is essential for calculating area?"},
                {"speaker": "B", "line": "The _____ dimension, not the slant side, because we need the perpendicular height."},
                {"speaker": "A", "line": "Excellent. Why is the area of a triangle exactly half the area of a rectangle?"},
                {"speaker": "B", "line": "Because a diagonal divides a rectangle into _____ equal triangles."},
                {"speaker": "A", "line": "Well reasoned. You demonstrate strong understanding of polygon area formulas."},
                {"speaker": "B", "line": "I appreciate your thorough teaching."}
            ]
        }
    },
    "surface area and volume": {
        "grade": 6,
        "social": {
            "title": "Building Shapes and Filling Boxes",
            "vocabulary": ["surface area", "volume", "face", "cube", "rectangular prism", "cubic units"],
            "script": [
                {"speaker": "A", "line": "Imagine a box. Do you know the difference between surface area and volume?"},
                {"speaker": "B", "line": "Not really. What's the difference?"},
                {"speaker": "A", "line": "Surface area is the _____ on the outside. Volume is how much _____ fits inside."},
                {"speaker": "B", "line": "Oh! So I use surface area to wrap a gift, and volume to fill it?"},
                {"speaker": "A", "line": "Exactly! If a box is 2 by 3 by 4, the volume is _____ cubic units."},
                {"speaker": "B", "line": "That's 2 times 3 times 4, so _____ cubic units!"},
                {"speaker": "A", "line": "Perfect! You really understand now!"},
                {"speaker": "B", "line": "This was really helpful!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Surface Area and Volume",
            "vocabulary": ["surface area", "volume", "base", "lateral faces", "cubic units", "rectangular prism"],
            "script": [
                {"speaker": "A", "line": "Good afternoon. We will explore surface area and volume."},
                {"speaker": "B", "line": "I am prepared to investigate."},
                {"speaker": "A", "line": "What is the formula for the volume of a rectangular prism?"},
                {"speaker": "B", "line": "Volume equals _____ times _____ times _____."},
                {"speaker": "A", "line": "Correct. Now, what does surface area represent, and how is it calculated?"},
                {"speaker": "B", "line": "Surface area is the total _____ of all faces. We find the area of each face and _____ them."},
                {"speaker": "A", "line": "Precisely. For a cube with side length 5, what is the total surface area?"},
                {"speaker": "B", "line": "A cube has 6 faces, each with area 5² = 25, so total surface area is _____."},
                {"speaker": "A", "line": "Excellent. Your understanding of three-dimensional measure is solid."},
                {"speaker": "B", "line": "Thank you for this systematic approach."}
            ]
        }
    },
    "statistical distributions": {
        "grade": 6,
        "social": {
            "title": "Looking at Data",
            "vocabulary": ["data", "distribution", "spread", "cluster", "pattern", "peak"],
            "script": [
                {"speaker": "A", "line": "Do you know what data is?"},
                {"speaker": "B", "line": "It's information we collect, right?"},
                {"speaker": "A", "line": "Yes! And how the data spreads out is called the distribution. Can you look at this list: 1, 2, 2, 3, 3, 3, 4?"},
                {"speaker": "B", "line": "It looks like most numbers are around _____?"},
                {"speaker": "A", "line": "Right! That's the peak. Is the data spread out or clustered together?"},
                {"speaker": "B", "line": "It's _____ together because the numbers don't go from 1 to 100."},
                {"speaker": "A", "line": "Great! You understand distributions!"},
                {"speaker": "B", "line": "This data stuff makes sense now!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Statistical Distributions",
            "vocabulary": ["distribution", "frequency", "center", "spread", "symmetrical", "skewed"],
            "script": [
                {"speaker": "A", "line": "Good morning. Let us analyze data distributions."},
                {"speaker": "B", "line": "I am ready to explore data."},
                {"speaker": "A", "line": "When we examine a distribution, what do we observe about where the data clusters?"},
                {"speaker": "B", "line": "We look for the _____, which is where most of the data points are located."},
                {"speaker": "A", "line": "Correct. What does spread tell us about the data?"},
                {"speaker": "B", "line": "Spread shows how _____ or _____ the data is from the center."},
                {"speaker": "A", "line": "Good. Is a distribution with all values clustered tightly more or less variable?"},
                {"speaker": "B", "line": "It is _____ variable because the data points are close together."},
                {"speaker": "A", "line": "Excellent reasoning. You understand distributions and variability."},
                {"speaker": "B", "line": "This statistical perspective is enlightening."}
            ]
        }
    },
    "measures of center": {
        "grade": 6,
        "social": {
            "title": "Finding the Middle of Data",
            "vocabulary": ["mean", "median", "mode", "average", "middle", "most common"],
            "script": [
                {"speaker": "A", "line": "Let's say you have test scores: 85, 90, 95, 100. What's the average?"},
                {"speaker": "B", "line": "Do I add them up?"},
                {"speaker": "A", "line": "Yes! Add them and divide by how many scores there are. What's the mean?"},
                {"speaker": "B", "line": "85 + 90 + 95 + 100 = _____, divided by 4 equals _____?"},
                {"speaker": "A", "line": "Perfect! That's the mean. Now, what's the median, or middle value?"},
                {"speaker": "B", "line": "The median is _____ because it's in the middle of 90 and 95."},
                {"speaker": "A", "line": "Excellent! You found both the mean and median!"},
                {"speaker": "B", "line": "These measures of center are really useful!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Measures of Center",
            "vocabulary": ["mean", "median", "mode", "average", "central tendency", "ordered set"],
            "script": [
                {"speaker": "A", "line": "Good morning. We will discuss measures of central tendency."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "Given the data set 3, 5, 5, 7, 10, what is the mean?"},
                {"speaker": "B", "line": "The mean is _____ + 5 + 5 + 7 + 10 divided by _____ = _____."},
                {"speaker": "A", "line": "Correct. What is the median, and why is order important?"},
                {"speaker": "B", "line": "The median is _____ because the data must be ordered from least to greatest first."},
                {"speaker": "A", "line": "Well stated. When is the mean not representative of the data?"},
                {"speaker": "B", "line": "The mean is not representative when there are _____, which pull the average away from the center."},
                {"speaker": "A", "line": "Excellent. You understand when different measures are appropriate."},
                {"speaker": "B", "line": "Thank you for this insightful discussion."}
            ]
        }
    },
    "proportional relationships": {
        "grade": 7,
        "social": {
            "title": "Comparing Things That Grow Together",
            "vocabulary": ["proportional", "constant", "ratio", "double", "scale"],
            "script": [
                {"speaker": "A", "line": "Do you know what proportional means?"},
                {"speaker": "B", "line": "Not really. Can you explain?"},
                {"speaker": "A", "line": "When two things grow together at the same rate. Like, for every 2 hours, you read 50 pages."},
                {"speaker": "B", "line": "So if you read for 4 hours, you'd read _____ pages?"},
                {"speaker": "A", "line": "Exactly! The ratio stays the same. What about 6 hours?"},
                {"speaker": "B", "line": "That would be _____ pages, because it's 3 times as long."},
                {"speaker": "A", "line": "You've got it! This is proportional reasoning!"},
                {"speaker": "B", "line": "That actually makes a lot of sense!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Proportional Relationships",
            "vocabulary": ["proportional", "constant of proportionality", "equivalent ratios", "linear", "direct variation"],
            "script": [
                {"speaker": "A", "line": "Good morning. Let us examine proportional relationships."},
                {"speaker": "B", "line": "I am ready to learn."},
                {"speaker": "A", "line": "Two quantities are proportional if their ratio is always the same. If x and y are proportional, what is true?"},
                {"speaker": "B", "line": "The ratio y/x is always _____, which we call the constant of proportionality."},
                {"speaker": "A", "line": "Correct. If y = 3x, what is the constant of proportionality?"},
                {"speaker": "B", "line": "The constant is _____ because y divided by x always equals _____."},
                {"speaker": "A", "line": "Good. Why must a proportional relationship always pass through the origin?"},
                {"speaker": "B", "line": "Because when x = 0, y must equal _____, representing zero of both quantities."},
                {"speaker": "A", "line": "Excellent reasoning. You understand proportional relationships thoroughly."},
                {"speaker": "B", "line": "Your instruction has been most valuable."}
            ]
        }
    },
    "operations with rational numbers": {
        "grade": 7,
        "social": {
            "title": "Adding, Subtracting, Multiplying, and Dividing Decimals and Fractions",
            "vocabulary": ["rational number", "decimal", "fraction", "operation", "equivalent", "simplify"],
            "script": [
                {"speaker": "A", "line": "Can you add 1/4 + 1/2?"},
                {"speaker": "B", "line": "Do I need to make them the same?"},
                {"speaker": "A", "line": "Yes! They need the same denominator. What is 1/4 + 2/4?"},
                {"speaker": "B", "line": "That's _____, which simplifies to _____."},
                {"speaker": "A", "line": "Right! Now try -2/3 + 1/6. First, make the denominators the same."},
                {"speaker": "B", "line": "That's -4/6 + 1/6, which equals _____?"},
                {"speaker": "A", "line": "Perfect! You're really good at this!"},
                {"speaker": "B", "line": "Thanks! Now I understand!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Operations with Rational Numbers",
            "vocabulary": ["rational number", "decimal", "fraction", "common denominator", "algorithm", "integer"],
            "script": [
                {"speaker": "A", "line": "Good morning. Today we explore operations with rational numbers."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "To add -5/8 + 3/4, what must we do first?"},
                {"speaker": "B", "line": "We must find a _____ denominator, which is _____."},
                {"speaker": "A", "line": "Correct. Convert both fractions and add them."},
                {"speaker": "B", "line": "-5/8 + 6/8 = _____."},
                {"speaker": "A", "line": "Good. Now, what happens when we multiply 2/5 by -3/4?"},
                {"speaker": "B", "line": "We multiply numerators: 2 × (-3) = _____, and denominators: 5 × 4 = _____, so the answer is _____."},
                {"speaker": "A", "line": "Excellent. Why is the product negative?"},
                {"speaker": "B", "line": "Because one factor is positive and one is _____, and the product is always _____."},
                {"speaker": "A", "line": "Perfect understanding. You master rational number operations."},
                {"speaker": "B", "line": "This comprehensive approach aids my understanding."}
            ]
        }
    },
    "expressions and equivalent forms": {
        "grade": 7,
        "social": {
            "title": "Different Ways to Write the Same Thing",
            "vocabulary": ["equivalent", "expression", "expand", "factor", "simplify", "combine"],
            "script": [
                {"speaker": "A", "line": "Is 2x + 3x the same as 5x?"},
                {"speaker": "B", "line": "I think so? They look different though."},
                {"speaker": "A", "line": "They're equivalent! Both equal the same thing. Combine the like terms: 2x + 3x = _____?"},
                {"speaker": "B", "line": "Oh! That's 5x!"},
                {"speaker": "A", "line": "Exactly! Now, is 2(x + 3) the same as 2x + 6?"},
                {"speaker": "B", "line": "Yes! When you distribute the 2, you get _____ + _____."},
                {"speaker": "A", "line": "Great! You understand equivalent expressions!"},
                {"speaker": "B", "line": "I like seeing different ways to write things!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Expressions and Equivalent Forms",
            "vocabulary": ["equivalent expressions", "distributive property", "like terms", "factor", "expand", "simplify"],
            "script": [
                {"speaker": "A", "line": "Good morning. We shall work with equivalent expressions."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "Simplify 3(2x - 4) + 5x using the distributive property."},
                {"speaker": "B", "line": "First, I distribute: 3(2x) + 3(-4) = _____ - 12. Then I add 5x to get _____."},
                {"speaker": "A", "line": "Correct. Why can we combine 6x and 5x?"},
                {"speaker": "B", "line": "Because they are _____ terms with the same variable and exponent."},
                {"speaker": "A", "line": "Good. Factor 4x + 8."},
                {"speaker": "B", "line": "The greatest common factor is _____, so 4x + 8 = 4(_____ + _____)"},
                {"speaker": "A", "line": "Excellent. Why is it important to recognize equivalent forms?"},
                {"speaker": "B", "line": "Because different forms can _____ different properties or solutions to problems."},
                {"speaker": "A", "line": "Well reasoned. You understand expression equivalence thoroughly."},
                {"speaker": "B", "line": "Thank you for this structured learning."}
            ]
        }
    },
    "two-step equations": {
        "grade": 7,
        "social": {
            "title": "Solving Equations in Two Steps",
            "vocabulary": ["equation", "inverse operation", "isolate", "solve", "step", "check"],
            "script": [
                {"speaker": "A", "line": "Let's solve 2x + 5 = 13 together."},
                {"speaker": "B", "line": "How do I start?"},
                {"speaker": "A", "line": "First, subtract 5 from both sides. What do you get?"},
                {"speaker": "B", "line": "2x = _____, right?"},
                {"speaker": "A", "line": "Perfect! Now divide by 2."},
                {"speaker": "B", "line": "So x = _____?"},
                {"speaker": "A", "line": "Exactly! You solved a two-step equation!"},
                {"speaker": "B", "line": "That wasn't as hard as I thought!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Two-Step Equations",
            "vocabulary": ["equation", "inverse operation", "solution", "check", "algorithm", "order of operations"],
            "script": [
                {"speaker": "A", "line": "Good morning. Today we solve two-step equations."},
                {"speaker": "B", "line": "I am ready."},
                {"speaker": "A", "line": "Solve 3x - 7 = 14. What inverse operation must we apply first?"},
                {"speaker": "B", "line": "We add _____ to both sides to isolate the term with x."},
                {"speaker": "A", "line": "Good. Continue solving."},
                {"speaker": "B", "line": "3x = _____, so x = _____."},
                {"speaker": "A", "line": "Correct. Why should we check our solution?"},
                {"speaker": "B", "line": "We check to verify that when x = _____, the original equation is _____."},
                {"speaker": "A", "line": "Exactly. Verify: 3(7) - 7 = 21 - 7 = 14. Why does order of operations matter?"},
                {"speaker": "B", "line": "We must undo operations in _____ order: addition/subtraction first, then multiplication/division."},
                {"speaker": "A", "line": "Excellent. You master two-step equation solving."},
                {"speaker": "B", "line": "Your systematic instruction is very clear."}
            ]
        }
    },
    "scale drawings": {
        "grade": 7,
        "social": {
            "title": "Making Things Bigger or Smaller",
            "vocabulary": ["scale", "scale factor", "proportional", "model", "actual size", "ratio"],
            "script": [
                {"speaker": "A", "line": "Do you know what a scale drawing is?"},
                {"speaker": "B", "line": "Is it like a map?"},
                {"speaker": "A", "line": "Yes! It's a small version of something real. If the scale is 1 inch = 10 feet, and a room is 3 inches on the drawing, how big is the real room?"},
                {"speaker": "B", "line": "I multiply 3 by 10, so it's _____ feet?"},
                {"speaker": "A", "line": "Exactly! What if the scale factor is 2? How would the drawing change?"},
                {"speaker": "B", "line": "Everything would be _____ as big!"},
                {"speaker": "A", "line": "Perfect! You understand scale drawings!"},
                {"speaker": "B", "line": "Maps make way more sense now!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Scale Drawings",
            "vocabulary": ["scale", "scale factor", "proportion", "correspondence", "similar figures", "linear scale"],
            "script": [
                {"speaker": "A", "line": "Good morning. We will examine scale drawings."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "In a scale drawing with scale 1 cm = 5 m, if a distance is 8 cm on the drawing, what is the actual distance?"},
                {"speaker": "B", "line": "I set up the proportion: 1/5 = 8/x, so x = _____ meters."},
                {"speaker": "A", "line": "Correct. If the scale factor is 0.5, what does this mean?"},
                {"speaker": "B", "line": "The drawing is _____ the size of the original object."},
                {"speaker": "A", "line": "Good. Why must all corresponding lengths follow the same scale factor?"},
                {"speaker": "B", "line": "Because the _____ is preserved; the drawing remains proportional to the actual object."},
                {"speaker": "A", "line": "Excellent. Are angles in the scale drawing larger, smaller, or the same as the original?"},
                {"speaker": "B", "line": "Angles remain _____ because scale only affects linear dimensions, not angle measures."},
                {"speaker": "A", "line": "Perfect reasoning. You understand scale drawing proportions thoroughly."},
                {"speaker": "B", "line": "This instruction has been comprehensive."}
            ]
        }
    },
    "circumference and area": {
        "grade": 7,
        "social": {
            "title": "Measuring Circles",
            "vocabulary": ["circle", "circumference", "area", "radius", "diameter", "pi"],
            "script": [
                {"speaker": "A", "line": "Do you know how to find the circumference of a circle?"},
                {"speaker": "B", "line": "Is that like the perimeter?"},
                {"speaker": "A", "line": "Yes! It's the distance around the circle. The formula is C = πd, where d is the diameter. If d = 10, what's C?"},
                {"speaker": "B", "line": "C = π × 10 = about _____ units?"},
                {"speaker": "A", "line": "Right! Now, the area formula is A = πr². If the radius is 5, what's the area?"},
                {"speaker": "B", "line": "A = π × 5² = π × _____ = about _____ square units?"},
                {"speaker": "A", "line": "Excellent! You've got circle formulas!"},
                {"speaker": "B", "line": "Circles are awesome!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Circumference and Area of Circles",
            "vocabulary": ["circumference", "area", "radius", "diameter", "pi", "quadratic"],
            "script": [
                {"speaker": "A", "line": "Good morning. We shall explore circle measurements."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "What is the relationship between circumference and diameter?"},
                {"speaker": "B", "line": "Circumference = _____ × diameter, where pi is a _____ ratio."},
                {"speaker": "A", "line": "Precisely. If the circumference is 31.4, what is the radius?"},
                {"speaker": "B", "line": "If C = 31.4, then 31.4 = 2πr, so r = _____."},
                {"speaker": "A", "line": "Good. How does the area formula relate to circumference?"},
                {"speaker": "B", "line": "The area A = πr² is _____, whereas circumference C = 2πr is _____."},
                {"speaker": "A", "line": "Correct. If we double the radius, by what factor does the area increase?"},
                {"speaker": "B", "line": "The area increases by a factor of _____ because area depends on r _____."},
                {"speaker": "A", "line": "Excellent reasoning. You understand circular measurements thoroughly."},
                {"speaker": "B", "line": "Your detailed explanations are most appreciated."}
            ]
        }
    },
    "angle relationships": {
        "grade": 7,
        "social": {
            "title": "Understanding Angles",
            "vocabulary": ["angle", "acute", "obtuse", "right", "supplementary", "complementary", "vertical"],
            "script": [
                {"speaker": "A", "line": "Do you know about complementary angles?"},
                {"speaker": "B", "line": "Not really. What are they?"},
                {"speaker": "A", "line": "They add up to 90 degrees. If one angle is 35°, what's the complementary angle?"},
                {"speaker": "B", "line": "It's 90 - 35 = _____°?"},
                {"speaker": "A", "line": "Right! Now, what are supplementary angles?"},
                {"speaker": "B", "line": "Do they add up to something else?"},
                {"speaker": "A", "line": "Yes! They add up to 180°. If one angle is 120°, what's its supplement?"},
                {"speaker": "B", "line": "180 - 120 = _____°?"},
                {"speaker": "A", "line": "Perfect! You understand angle relationships!"},
                {"speaker": "B", "line": "Angles are easier now!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Angle Relationships",
            "vocabulary": ["angle", "complementary", "supplementary", "vertical angles", "adjacent", "straight angle"],
            "script": [
                {"speaker": "A", "line": "Good morning. Let us discuss angle relationships."},
                {"speaker": "B", "line": "I am ready."},
                {"speaker": "A", "line": "What are vertical angles, and what is their relationship?"},
                {"speaker": "B", "line": "Vertical angles are formed when two lines intersect, and they are always _____."},
                {"speaker": "A", "line": "Correct. If two supplementary angles have measures x and x + 30, what is x?"},
                {"speaker": "B", "line": "Since they sum to 180°: x + (x + 30) = 180, so 2x = _____, and x = _____."},
                {"speaker": "A", "line": "Good. Why are complementary angles always acute?"},
                {"speaker": "B", "line": "Because their sum is 90°, and if either were _____ or more, the other would be _____ or less, which is impossible."},
                {"speaker": "A", "line": "Excellent reasoning. When are adjacent angles supplementary?"},
                {"speaker": "B", "line": "Adjacent angles are supplementary when they form a _____ line."},
                {"speaker": "A", "line": "Perfect. You understand angle relationships thoroughly."},
                {"speaker": "B", "line": "Thank you for this precise instruction."}
            ]
        }
    },
    "probability": {
        "grade": 7,
        "social": {
            "title": "What Are the Chances?",
            "vocabulary": ["probability", "certain", "impossible", "unlikely", "likely", "outcome", "event"],
            "script": [
                {"speaker": "A", "line": "If you flip a coin, what are the chances of getting heads?"},
                {"speaker": "B", "line": "Is it 50%?"},
                {"speaker": "A", "line": "Yes! That's 1/2 or 0.5. We say the probability is _____. Now, if you roll a die, what's the probability of rolling a 3?"},
                {"speaker": "B", "line": "There's one 3 out of _____ sides, so it's _____?"},
                {"speaker": "A", "line": "Exactly! What's the probability of rolling a 7 on a standard die?"},
                {"speaker": "B", "line": "There's no 7, so the probability is _____ or _____. That's impossible!"},
                {"speaker": "A", "line": "Perfect! You understand probability!"},
                {"speaker": "B", "line": "That's actually pretty cool!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Probability",
            "vocabulary": ["probability", "theoretical", "experimental", "outcome", "sample space", "independent events"],
            "script": [
                {"speaker": "A", "line": "Good morning. Let us study probability."},
                {"speaker": "B", "line": "I am ready."},
                {"speaker": "A", "line": "What is the difference between theoretical and experimental probability?"},
                {"speaker": "B", "line": "Theoretical probability is _____, while experimental probability is based on _____ data."},
                {"speaker": "A", "line": "Correct. If you flip a coin 100 times and get 47 heads, what is the experimental probability?"},
                {"speaker": "B", "line": "The experimental probability is 47/100 = _____."},
                {"speaker": "A", "line": "Good. If you roll a die and flip a coin, how many outcomes are possible?"},
                {"speaker": "B", "line": "There are _____ outcomes for the die and _____ for the coin, so _____ total outcomes."},
                {"speaker": "A", "line": "Correct. Why do we say these are independent events?"},
                {"speaker": "B", "line": "Because the outcome of one event does not _____ the outcome of the other event."},
                {"speaker": "A", "line": "Excellent. You understand probability and independence."},
                {"speaker": "B", "line": "This clear explanation has been helpful."}
            ]
        }
    },
    "random sampling": {
        "grade": 7,
        "social": {
            "title": "Picking a Fair Sample",
            "vocabulary": ["sample", "random", "bias", "population", "representative", "fair"],
            "script": [
                {"speaker": "A", "line": "Do you know what random sampling is?"},
                {"speaker": "B", "line": "Is it when you pick things randomly?"},
                {"speaker": "A", "line": "Yes, but fairly! Every person or item should have an equal chance. If your school has 500 students and you want a sample of 50, how should you pick them?"},
                {"speaker": "B", "line": "You should pick them _____, not pick your friends?"},
                {"speaker": "A", "line": "Exactly! Picking your friends would be _____ because it's not fair."},
                {"speaker": "B", "line": "So random means everyone has an equal _____?"},
                {"speaker": "A", "line": "Perfect! You understand random sampling!"},
                {"speaker": "B", "line": "That makes sense for fair research!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Random Sampling",
            "vocabulary": ["random sample", "bias", "population", "sample", "representative", "systematic sampling"],
            "script": [
                {"speaker": "A", "line": "Good morning. We will discuss random sampling methods."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "What is bias in sampling, and why is it problematic?"},
                {"speaker": "B", "line": "Bias occurs when the sample does not _____ the population, leading to _____ conclusions."},
                {"speaker": "A", "line": "Correct. If you survey only people in a coffee shop about coffee preferences, what kind of bias occurs?"},
                {"speaker": "B", "line": "That is _____ bias because coffee drinkers are more likely to _____ coffee."},
                {"speaker": "A", "line": "Well stated. What makes a sample random and unbiased?"},
                {"speaker": "B", "line": "Every individual in the population must have an _____ and _____ chance of being selected."},
                {"speaker": "A", "line": "Good. How would you randomly select 30 students from 600?"},
                {"speaker": "B", "line": "I would assign each student a number and _____ 30 numbers using a random method."},
                {"speaker": "A", "line": "Excellent reasoning. You understand sampling principles thoroughly."},
                {"speaker": "B", "line": "This methodological understanding is invaluable."}
            ]
        }
    },
    "exponents and scientific notation": {
        "grade": 8,
        "social": {
            "title": "Big Numbers and Small Numbers",
            "vocabulary": ["exponent", "power", "base", "scientific notation", "standard form"],
            "script": [
                {"speaker": "A", "line": "What does 2³ mean?"},
                {"speaker": "B", "line": "Is it 2 times 3?"},
                {"speaker": "A", "line": "No, it means 2 times 2 times 2. What's the answer?"},
                {"speaker": "B", "line": "2 × 2 × 2 = _____?"},
                {"speaker": "A", "line": "Right! Now, scientists use scientific notation for really big numbers. 5,000,000,000 can be written as _____ × 10⁹."},
                {"speaker": "B", "line": "So the _____ tells us how many places to move the decimal?"},
                {"speaker": "A", "line": "Exactly! You understand exponents and scientific notation!"},
                {"speaker": "B", "line": "This helps me understand big numbers!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Exponents and Scientific Notation",
            "vocabulary": ["exponent", "base", "power", "scientific notation", "coefficient", "order of magnitude"],
            "script": [
                {"speaker": "A", "line": "Good morning. Today we explore exponents and scientific notation."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "Simplify 3² × 3⁴ using exponent rules."},
                {"speaker": "B", "line": "Using the product rule: 3² × 3⁴ = 3^_____ = _____."},
                {"speaker": "A", "line": "Correct. What is 5⁰, and why?"},
                {"speaker": "B", "line": "Any nonzero number to the zero power equals _____."},
                {"speaker": "A", "line": "Good. Convert 245,000,000 to scientific notation."},
                {"speaker": "B", "line": "In scientific notation: _____ × 10⁸, because the decimal moves _____ places."},
                {"speaker": "A", "line": "Correct. If we have 3 × 10⁻⁴, what is the standard form?"},
                {"speaker": "B", "line": "The negative exponent means we move the decimal _____ places: _____."},
                {"speaker": "A", "line": "Excellent. Why is scientific notation useful?"},
                {"speaker": "B", "line": "It makes very large and very _____ numbers easier to _____ and compare."},
                {"speaker": "A", "line": "Well reasoned. You master exponents and scientific notation."},
                {"speaker": "B", "line": "Thank you for this comprehensive lesson."}
            ]
        }
    },
    "square roots and irrational numbers": {
        "grade": 8,
        "social": {
            "title": "Perfect Squares and Numbers That Don't Repeat",
            "vocabulary": ["square root", "perfect square", "irrational", "rational", "radical", "approximate"],
            "script": [
                {"speaker": "A", "line": "What's the square root of 16?"},
                {"speaker": "B", "line": "Is it a number that makes 4?"},
                {"speaker": "A", "line": "Yes! What number times itself equals 16?"},
                {"speaker": "B", "line": "4 × 4 = 16, so √16 = _____?"},
                {"speaker": "A", "line": "Perfect! Now, what about √2?"},
                {"speaker": "B", "line": "Um, is that a whole number?"},
                {"speaker": "A", "line": "No. √2 is about 1.414..., and it never repeats. That's an irrational number!"},
                {"speaker": "B", "line": "Oh! So some square roots are rational and some are _____!"},
                {"speaker": "A", "line": "Exactly! You're getting it!"},
                {"speaker": "B", "line": "That's really interesting!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Square Roots and Irrational Numbers",
            "vocabulary": ["square root", "perfect square", "irrational number", "rational number", "radical", "non-terminating"],
            "script": [
                {"speaker": "A", "line": "Good morning. We shall examine square roots and irrational numbers."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "What distinguishes a rational number from an irrational number?"},
                {"speaker": "B", "line": "A rational number can be expressed as a _____, while an irrational number _____."},
                {"speaker": "A", "line": "Correct. Is √25 rational or irrational, and why?"},
                {"speaker": "B", "line": "√25 = _____, which is an integer, so it is _____."},
                {"speaker": "A", "line": "Good. What about √10?"},
                {"speaker": "B", "line": "√10 is between _____ and _____, and cannot be expressed as a fraction, so it is _____."},
                {"speaker": "A", "line": "Excellent. Simplify √72."},
                {"speaker": "B", "line": "I find the largest perfect square factor: 72 = _____ × 2, so √72 = _____."},
                {"speaker": "A", "line": "Perfect. Why is π irrational?"},
                {"speaker": "B", "line": "Because π is _____ and does not repeat, so it cannot be written as a fraction."},
                {"speaker": "A", "line": "Excellent understanding. You master square roots and irrational numbers."},
                {"speaker": "B", "line": "Your instruction has been illuminating."}
            ]
        }
    },
    "linear functions": {
        "grade": 8,
        "social": {
            "title": "Lines That Show Patterns",
            "vocabulary": ["function", "linear", "slope", "y-intercept", "graph", "relationship"],
            "script": [
                {"speaker": "A", "line": "Do you know what a linear function is?"},
                {"speaker": "B", "line": "Is it something to do with lines?"},
                {"speaker": "A", "line": "Yes! It's a pattern that makes a straight line on a graph. The equation y = 2x + 1 is linear."},
                {"speaker": "B", "line": "What does the 2 mean?"},
                {"speaker": "A", "line": "That's the slope. For every 1 unit right, you go _____ units up."},
                {"speaker": "B", "line": "And the 1 is the y-intercept, where the line crosses the _____?"},
                {"speaker": "A", "line": "Perfect! You understand linear functions!"},
                {"speaker": "B", "line": "Patterns make so much sense now!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Linear Functions",
            "vocabulary": ["linear function", "slope", "y-intercept", "rate of change", "domain", "range"],
            "script": [
                {"speaker": "A", "line": "Good morning. We explore linear functions."},
                {"speaker": "B", "line": "I am ready."},
                {"speaker": "A", "line": "What is the slope of the line passing through (2, 5) and (6, 13)?"},
                {"speaker": "B", "line": "Using the slope formula: m = (13 - 5)/(6 - 2) = _____/_____  = _____."},
                {"speaker": "A", "line": "Correct. What does this slope represent?"},
                {"speaker": "B", "line": "It represents the _____ of change; for every 1 unit increase in x, y increases by _____."},
                {"speaker": "A", "line": "Good. Write the equation in slope-intercept form using slope 2 and y-intercept 3."},
                {"speaker": "B", "line": "The equation is y = _____x + _____."},
                {"speaker": "A", "line": "Correct. What is the domain and range of a linear function?"},
                {"speaker": "B", "line": "For a linear function, both domain and range are typically all _____ numbers."},
                {"speaker": "A", "line": "Excellent. You understand linear functions thoroughly."},
                {"speaker": "B", "line": "Thank you for this detailed instruction."}
            ]
        }
    },
    "systems of equations": {
        "grade": 8,
        "social": {
            "title": "Finding Where Two Equations Meet",
            "vocabulary": ["system", "equation", "solution", "intersection", "substitute", "eliminate"],
            "script": [
                {"speaker": "A", "line": "What's a system of equations?"},
                {"speaker": "B", "line": "Is it more than one equation?"},
                {"speaker": "A", "line": "Yes! We solve them together. If y = 2x and y = x + 3, what is x?"},
                {"speaker": "B", "line": "Since both equal y, then 2x = x + 3, so x = _____?"},
                {"speaker": "A", "line": "Right! What is y?"},
                {"speaker": "B", "line": "If x = 3, then y = 2(3) = _____ or y = 3 + 3 = _____?"},
                {"speaker": "A", "line": "Perfect! You solved a system!"},
                {"speaker": "B", "line": "That was actually logical!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Systems of Equations",
            "vocabulary": ["system", "solution", "substitution", "elimination", "intersection", "consistent"],
            "script": [
                {"speaker": "A", "line": "Good morning. We shall solve systems of equations."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "Solve the system: 2x + y = 7 and x - y = 2. What method would you use?"},
                {"speaker": "B", "line": "I would use the _____ method since the y terms are opposites."},
                {"speaker": "A", "line": "Good. Add the equations and solve for x."},
                {"speaker": "B", "line": "Adding: 3x = _____, so x = _____."},
                {"speaker": "A", "line": "Correct. Now substitute to find y."},
                {"speaker": "B", "line": "Using x - y = 2: _____ - y = 2, so y = _____."},
                {"speaker": "A", "line": "Good. Verify this solution in both equations. Why is it necessary?"},
                {"speaker": "B", "line": "Verification ensures the solution satisfies _____ equations simultaneously."},
                {"speaker": "A", "line": "Excellent. You understand systems of equations thoroughly."},
                {"speaker": "B", "line": "This systematic approach is very effective."}
            ]
        }
    },
    "multi-step equations": {
        "grade": 8,
        "social": {
            "title": "Solving More Complicated Equations",
            "vocabulary": ["equation", "distribute", "combine", "isolate", "variable", "inverse"],
            "script": [
                {"speaker": "A", "line": "Let's solve 3(x + 2) - 5 = 10. Can you start?"},
                {"speaker": "B", "line": "Do I distribute the 3 first?"},
                {"speaker": "A", "line": "Yes! What do you get?"},
                {"speaker": "B", "line": "3x + _____ - 5 = 10?"},
                {"speaker": "A", "line": "Good! Now combine like terms."},
                {"speaker": "B", "line": "3x + _____ = 10?"},
                {"speaker": "A", "line": "Right! Now isolate x."},
                {"speaker": "B", "line": "3x = _____, so x = _____?"},
                {"speaker": "A", "line": "Perfect! You solved a multi-step equation!"},
                {"speaker": "B", "line": "I did it! This is so cool!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Multi-Step Equations",
            "vocabulary": ["multi-step equation", "distributive property", "like terms", "inverse operation", "solution"],
            "script": [
                {"speaker": "A", "line": "Good morning. Today we solve multi-step equations."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "Solve 2(3x - 4) + 5 = 19. What is the first step?"},
                {"speaker": "B", "line": "Apply the _____ property to distribute the 2."},
                {"speaker": "A", "line": "Good. Continue."},
                {"speaker": "B", "line": "6x - 8 + 5 = 19, which simplifies to 6x _____ = 19."},
                {"speaker": "A", "line": "Correct. Isolate the variable."},
                {"speaker": "B", "line": "6x = _____, so x = _____."},
                {"speaker": "A", "line": "Correct. Why must we follow the correct order of steps?"},
                {"speaker": "B", "line": "Because _____ in solving just like in _____, order matters for correct results."},
                {"speaker": "A", "line": "Excellent. You understand multi-step equation solving."},
                {"speaker": "B", "line": "Thank you for this structured approach."}
            ]
        }
    },
    "pythagorean theorem": {
        "grade": 8,
        "social": {
            "title": "Right Triangles and Sides",
            "vocabulary": ["Pythagorean theorem", "right triangle", "legs", "hypotenuse", "a²+b²=c²"],
            "script": [
                {"speaker": "A", "line": "Do you know about the Pythagorean theorem?"},
                {"speaker": "B", "line": "Is that something with triangles?"},
                {"speaker": "A", "line": "Yes! For right triangles, a² + b² = c², where c is the longest side. If the legs are 3 and 4, what's the hypotenuse?"},
                {"speaker": "B", "line": "3² + 4² = c², so 9 + 16 = c², which means c² = _____, so c = _____?"},
                {"speaker": "A", "line": "Perfect! Now, if one leg is 5 and the hypotenuse is 13, what's the other leg?"},
                {"speaker": "B", "line": "5² + b² = 13², so 25 + b² = _____, which means b² = _____, so b = _____?"},
                {"speaker": "A", "line": "Excellent! You've got the Pythagorean theorem!"},
                {"speaker": "B", "line": "That's such a cool formula!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Pythagorean Theorem",
            "vocabulary": ["Pythagorean theorem", "hypotenuse", "leg", "right triangle", "distance", "converse"],
            "script": [
                {"speaker": "A", "line": "Good morning. We explore the Pythagorean theorem."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "State the Pythagorean theorem and explain when it applies."},
                {"speaker": "B", "line": "In a right triangle, a² + b² = c², where c is the _____ and a and b are the _____."},
                {"speaker": "A", "line": "Correct. Find the length of the hypotenuse of a right triangle with legs 7 and 24."},
                {"speaker": "B", "line": "c² = 7² + 24² = _____ + _____ = _____, so c = _____."},
                {"speaker": "A", "line": "Good. How can we use the Pythagorean theorem to find distance?"},
                {"speaker": "B", "line": "We treat the horizontal and vertical distances as _____ and find the _____ distance using c."},
                {"speaker": "A", "line": "Excellent. What is the converse of the Pythagorean theorem?"},
                {"speaker": "B", "line": "If a² + b² = c², then the triangle is a _____ triangle with hypotenuse c."},
                {"speaker": "A", "line": "Perfect. You understand the Pythagorean theorem thoroughly."},
                {"speaker": "B", "line": "This instruction has been most valuable."}
            ]
        }
    },
    "transformations": {
        "grade": 8,
        "social": {
            "title": "Moving and Flipping Shapes",
            "vocabulary": ["transformation", "translation", "rotation", "reflection", "congruent", "coordinate"],
            "script": [
                {"speaker": "A", "line": "Do you know what a transformation is?"},
                {"speaker": "B", "line": "Is it changing a shape?"},
                {"speaker": "A", "line": "Yes! There are different types. A translation slides a shape. If we slide a triangle 3 units right and 2 units up, what happens to its size and shape?"},
                {"speaker": "B", "line": "The size and shape stay the _____?"},
                {"speaker": "A", "line": "Exactly! A reflection flips a shape over a line. A rotation turns it around a point."},
                {"speaker": "B", "line": "Do all three keep the shape the same size?"},
                {"speaker": "A", "line": "Yes! They're called rigid transformations. You understand transformations!"},
                {"speaker": "B", "line": "That makes sense!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Transformations",
            "vocabulary": ["transformation", "translation", "rotation", "reflection", "rigid", "congruent", "image"],
            "script": [
                {"speaker": "A", "line": "Good morning. We examine transformations."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "What characterizes a rigid transformation?"},
                {"speaker": "B", "line": "A rigid transformation preserves _____ and _____, mapping the figure to a _____ image."},
                {"speaker": "A", "line": "Correct. If point (2, 3) is translated by the rule (x + 4, y - 2), what is the image?"},
                {"speaker": "B", "line": "The image is at (_____,_____)"},
                {"speaker": "A", "line": "Good. What is a reflection over the y-axis?"},
                {"speaker": "B", "line": "A reflection over the y-axis maps (x, y) to (_____,_____)."},
                {"speaker": "A", "line": "Correct. A 90° rotation counterclockwise around the origin maps (x, y) to what?"},
                {"speaker": "B", "line": "A 90° counterclockwise rotation maps (x, y) to (_____,_____)."},
                {"speaker": "A", "line": "Excellent. You understand transformations thoroughly."},
                {"speaker": "B", "line": "Thank you for this precise instruction."}
            ]
        }
    },
    "congruence and similarity": {
        "grade": 8,
        "social": {
            "title": "Same Shape, Different Size",
            "vocabulary": ["congruent", "similar", "corresponding", "scale factor", "angles", "proportional"],
            "script": [
                {"speaker": "A", "line": "What's the difference between congruent and similar shapes?"},
                {"speaker": "B", "line": "Are they the same thing?"},
                {"speaker": "A", "line": "Not quite. Congruent shapes are exactly the same size and shape. Similar shapes have the same shape but different _____?"},
                {"speaker": "B", "line": "So similar shapes are like _____?"},
                {"speaker": "A", "line": "Yes! If triangle ABC is similar to triangle DEF with a scale factor of 2, and AB = 3, what is DE?"},
                {"speaker": "B", "line": "DE = 3 × _____ = _____?"},
                {"speaker": "A", "line": "Perfect! You understand congruence and similarity!"},
                {"speaker": "B", "line": "That's a useful difference to know!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Congruence and Similarity",
            "vocabulary": ["congruent", "similar", "corresponding sides", "scale factor", "correspondence", "AA criterion"],
            "script": [
                {"speaker": "A", "line": "Good morning. We explore congruence and similarity."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "What criteria establish that two triangles are congruent?"},
                {"speaker": "B", "line": "SSS, SAS, and _____ are congruence criteria."},
                {"speaker": "A", "line": "Correct. What makes two figures similar?"},
                {"speaker": "B", "line": "Two figures are similar if _____ angles are equal and _____ sides are proportional."},
                {"speaker": "A", "line": "Good. If triangle ABC has sides 3, 4, 5 and is similar to triangle DEF with scale factor 3, what are the sides of DEF?"},
                {"speaker": "B", "line": "The sides are _____, _____, and _____."},
                {"speaker": "A", "line": "Correct. Why is AA similarity sufficient for triangles?"},
                {"speaker": "B", "line": "If two angles are equal, the third angle is also _____, so all angles are equal and sides are _____."},
                {"speaker": "A", "line": "Excellent reasoning. You understand congruence and similarity."},
                {"speaker": "B", "line": "This instruction is comprehensive."}
            ]
        }
    },
    "volume of cylinders cones spheres": {
        "grade": 8,
        "social": {
            "title": "How Much Fits Inside Three-Dimensional Shapes",
            "vocabulary": ["volume", "cylinder", "cone", "sphere", "radius", "height", "cubic units"],
            "script": [
                {"speaker": "A", "line": "Do you know how to find the volume of a cylinder?"},
                {"speaker": "B", "line": "Is it the same as a rectangular box?"},
                {"speaker": "A", "line": "Not quite. For a cylinder, the formula is V = πr²h. If the radius is 3 and height is 10, what's the volume?"},
                {"speaker": "B", "line": "V = π × 3² × 10 = π × _____ × 10 = _____ cubic units?"},
                {"speaker": "A", "line": "Right! A cone has the same base but comes to a point. Is its volume bigger or smaller than a cylinder?"},
                {"speaker": "B", "line": "A cone is smaller because the formula is _____ the cylinder's volume?"},
                {"speaker": "A", "line": "Exactly! And a sphere uses the formula V = (4/3)πr³."},
                {"speaker": "B", "line": "Wow, there are so many formulas!"},
                {"speaker": "A", "line": "But now you understand them!"},
                {"speaker": "B", "line": "These 3D shapes are cool!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Volume of Cylinders, Cones, and Spheres",
            "vocabulary": ["volume", "cylinder", "cone", "sphere", "base area", "radius", "height"],
            "script": [
                {"speaker": "A", "line": "Good morning. We calculate volumes of 3D shapes."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "What is the formula for the volume of a cylinder?"},
                {"speaker": "B", "line": "V = _____ × height, where the base is a circle with area πr²."},
                {"speaker": "A", "line": "Correct. How does the volume of a cone compare to a cylinder with the same base and height?"},
                {"speaker": "B", "line": "The cone's volume is _____ of the cylinder's volume."},
                {"speaker": "A", "line": "Good. What is the formula for the volume of a cone?"},
                {"speaker": "B", "line": "V = (1/3)πr²h."},
                {"speaker": "A", "line": "Correct. What is the formula for a sphere?"},
                {"speaker": "B", "line": "V = (4/3)πr³."},
                {"speaker": "A", "line": "Good. A cylinder has radius 4 and height 8. Find its volume."},
                {"speaker": "B", "line": "V = π(4)²(8) = _____ π cubic units."},
                {"speaker": "A", "line": "Excellent. You master volume calculations."},
                {"speaker": "B", "line": "Thank you for this detailed instruction."}
            ]
        }
    },
    "scatter plots": {
        "grade": 8,
        "social": {
            "title": "Showing Relationships with Dots",
            "vocabulary": ["scatter plot", "data point", "relationship", "correlation", "trend line", "positive", "negative"],
            "script": [
                {"speaker": "A", "line": "Do you know what a scatter plot is?"},
                {"speaker": "B", "line": "It's just dots, right?"},
                {"speaker": "A", "line": "Yes, but the dots show a relationship between two variables. If we plot study hours versus test scores, what relationship might we see?"},
                {"speaker": "B", "line": "More study hours should mean _____ test scores?"},
                {"speaker": "A", "line": "Exactly! That's a positive relationship. We can draw a trend line through the dots. Why is that helpful?"},
                {"speaker": "B", "line": "Because we can see the _____ and predict values?"},
                {"speaker": "A", "line": "Perfect! You understand scatter plots!"},
                {"speaker": "B", "line": "That's useful!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Scatter Plots",
            "vocabulary": ["scatter plot", "correlation", "positive correlation", "negative correlation", "trend line", "linear relationship"],
            "script": [
                {"speaker": "A", "line": "Good morning. We analyze scatter plots."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "What does a scatter plot display?"},
                {"speaker": "B", "line": "A scatter plot shows the _____ between two _____ variables using ordered pairs."},
                {"speaker": "A", "line": "Correct. If a scatter plot shows points trending upward from left to right, what type of correlation exists?"},
                {"speaker": "B", "line": "This is a _____ correlation, meaning as one variable increases, the other _____."},
                {"speaker": "A", "line": "Good. What is a trend line?"},
                {"speaker": "B", "line": "A trend line is a _____ drawn through the data points to show the overall _____."},
                {"speaker": "A", "line": "Correct. Can we use a trend line to make predictions?"},
                {"speaker": "B", "line": "Yes, we can use the trend line to _____ values for x or y values not in the data."},
                {"speaker": "A", "line": "Excellent. You understand scatter plots and correlation."},
                {"speaker": "B", "line": "This instruction has been valuable."}
            ]
        }
    },
    "two-way frequency tables": {
        "grade": 8,
        "social": {
            "title": "Organizing Data in Tables",
            "vocabulary": ["two-way table", "frequency", "category", "row", "column", "relative frequency"],
            "script": [
                {"speaker": "A", "line": "Do you know what a two-way frequency table is?"},
                {"speaker": "B", "line": "Is it a table with data?"},
                {"speaker": "A", "line": "Yes! It shows the relationship between two categories. Like, 'Do you play sports?' and 'Are you in band?' Let's say 40 students play sports and are in band."},
                {"speaker": "B", "line": "So we put 40 in the right _____ of the table?"},
                {"speaker": "A", "line": "Exactly! We can also find relative frequency. If 100 students total and 40 play sports AND are in band, the relative frequency is _____?"},
                {"speaker": "B", "line": "40/100 = _____ or _____% ?"},
                {"speaker": "A", "line": "Perfect! You understand two-way tables!"},
                {"speaker": "B", "line": "Tables make data so clear!"}
            ]
        },
        "academic": {
            "title": "Mathematical Discussion: Two-Way Frequency Tables",
            "vocabulary": ["two-way frequency table", "frequency", "relative frequency", "marginal frequency", "conditional frequency"],
            "script": [
                {"speaker": "A", "line": "Good morning. We analyze two-way frequency tables."},
                {"speaker": "B", "line": "I am prepared."},
                {"speaker": "A", "line": "What information does a two-way frequency table convey?"},
                {"speaker": "B", "line": "It displays frequencies of _____ variables organized by rows and _____."},
                {"speaker": "A", "line": "Correct. What is a marginal frequency?"},
                {"speaker": "B", "line": "A marginal frequency is the _____ of a row or column, found in the _____ row or column."},
                {"speaker": "A", "line": "Good. What is conditional frequency?"},
                {"speaker": "B", "line": "Conditional frequency is the _____ of one event given that another event _____."},
                {"speaker": "A", "line": "Correct. If 50 students prefer math, and 30 of them are female, what is the conditional frequency?"},
                {"speaker": "B", "line": "The conditional frequency is 30/50 = _____."},
                {"speaker": "A", "line": "Excellent. You understand frequency tables thoroughly."},
                {"speaker": "B", "line": "Thank you for this detailed instruction."}
            ]
        }
    }
}
LEVELED_PROBLEMS_COMPLETE = {
    "ratios and rates": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "A bag has 3 red marbles and 5 blue marbles. What is the ratio of red marbles to blue marbles?", "answer": "3:5"},
                {"problem": "For every 2 apples, there is 1 orange. Draw a picture showing this ratio.", "answer": "Picture showing 2 apples and 1 orange (or multiples like 4 apples and 2 oranges)"},
                {"problem": "If you run 5 miles in 1 hour, what is your speed?", "answer": "5 miles per hour (mph)"}
            ],
            "developing": [
                {"problem": "A recipe calls for 2 cups of flour and 3 cups of sugar. What is the ratio of flour to total ingredients?", "answer": "2:5"},
                {"problem": "A car travels 150 miles in 3 hours. What is the unit rate (miles per hour)?", "answer": "50 miles per hour"},
                {"problem": "Two stores sell the same juice. Store A sells 8 bottles for $12. Store B sells 5 bottles for $8. Which store has the better rate?", "answer": "Store B ($1.60 per bottle vs $1.50 per bottle)"}
            ],
            "proficient": [
                {"problem": "A recipe serves 4 people and uses 2 cups of flour, 1 cup of sugar, and 3/4 cup of butter. If you want to serve 10 people, how much of each ingredient do you need?", "answer": "5 cups flour, 2.5 cups sugar, 1.875 cups butter"},
                {"problem": "A map has a scale of 1 inch : 25 miles. If two cities are 4.5 inches apart on the map, how far apart are they in reality?", "answer": "112.5 miles"},
                {"problem": "Company A pays $15 per hour with no bonus. Company B pays $12 per hour plus a $100 monthly bonus. If you work 160 hours per month, which company pays more? By how much?", "answer": "Company A pays $2400; Company B pays $2020. Company A pays $380 more."}
            ],
            "extending": [
                {"problem": "A smoothie shop makes drinks with ratios: 3 parts fruit, 2 parts yogurt, 1 part honey. If you want a drink with 12 ounces of total ingredients, and you want the ratio to remain the same, how much of each ingredient is needed? What would happen if you tripled the recipe?", "answer": "Original: 6 oz fruit, 4 oz yogurt, 2 oz honey. Tripled: 18 oz fruit, 12 oz yogurt, 6 oz honey. The ratio stays 3:2:1 because all amounts scale equally."},
                {"problem": "Two athletes train at different rates. Athlete A runs 2 miles in 16 minutes. Athlete B runs 3 miles in 24 minutes. Which athlete is faster? Explain why comparing unit rates is better than just comparing the numbers given.", "answer": "Athlete A: 7.5 mph; Athlete B: 7.5 mph. They run at the same speed. Unit rates let us compare fairly because the distances and times were different."},
                {"problem": "If 15 workers can complete a job in 8 days, how many workers are needed to complete the same job in 5 days? Explain your reasoning.", "answer": "24 workers. The job requires 120 worker-days (15 × 8). To complete it in 5 days: 120 ÷ 5 = 24 workers. This is an inverse ratio—as time decreases, workers needed increase."}
            ]
        }
    },
    "division of fractions": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "How many 1/4 pieces are in 1 whole? Use a picture to help.", "answer": "4"},
                {"problem": "Calculate: 1/2 ÷ 1/4", "answer": "2"},
                {"problem": "If you have 3 meters of ribbon and cut it into pieces that are 1/3 meter long, how many pieces do you get?", "answer": "9 pieces"}
            ],
            "developing": [
                {"problem": "Calculate: 3/4 ÷ 1/8", "answer": "6"},
                {"problem": "A baker has 5 cups of flour. Each batch of cookies uses 3/4 cup. How many complete batches can they make?", "answer": "6 complete batches (6 remainder 2/3)"},
                {"problem": "Calculate: 2/5 ÷ 2/3", "answer": "3/5"}
            ],
            "proficient": [
                {"problem": "Calculate: 4 1/2 ÷ 3/4. Explain each step.", "answer": "Convert to improper fraction: 9/2 ÷ 3/4 = 9/2 × 4/3 = 36/6 = 6"},
                {"problem": "A runner has 8 miles left to run. If they stop every 2/5 miles to stretch, how many times will they stop?", "answer": "20 times (8 ÷ 2/5 = 8 × 5/2 = 20)"},
                {"problem": "Calculate: 5/6 ÷ 1/3 + 1/2. Show your work.", "answer": "5/6 ÷ 1/3 = 5/2 = 2.5; 2.5 + 0.5 = 3"}
            ],
            "extending": [
                {"problem": "A tailor is cutting fabric. She has 10 1/4 yards of material. Each garment needs 1 3/8 yards. How many complete garments can she make, and how much fabric is left over? Explain why division of fractions applies here.", "answer": "10 1/4 ÷ 1 3/8 = 41/4 ÷ 11/8 = 41/4 × 8/11 = 328/44 = 7 20/44 = 7 5/11. She can make 7 complete garments with 5/11 yards remaining. Division tells us how many equal groups we can make."},
                {"problem": "If 2/3 of a number equals 12, what is the number? Solve this using division of fractions and verify your answer.", "answer": "12 ÷ 2/3 = 12 × 3/2 = 18. Check: 2/3 × 18 = 12. ✓"},
                {"problem": "Create a word problem that would be solved by 3 3/4 ÷ 1/2. Solve it and explain why the answer is larger than the dividend.", "answer": "Example: 'I have 3 3/4 gallons of paint. Each room needs 1/2 gallon. How many rooms can I paint?' Answer: 7 1/2 rooms. The answer is larger because we're dividing by a number smaller than 1, which means we get more groups."}
            ]
        }
    },
    "positive and negative numbers": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "The temperature is 5 degrees. It drops 8 degrees. What is the new temperature?", "answer": "-3 degrees"},
                {"problem": "Order these numbers from least to greatest: 2, -1, 0, -3", "answer": "-3, -1, 0, 2"},
                {"problem": "A submarine is at 200 feet below sea level. Write this as an integer.", "answer": "-200"}
            ],
            "developing": [
                {"problem": "Calculate: -5 + 3", "answer": "-2"},
                {"problem": "Calculate: -2 - (-4)", "answer": "2"},
                {"problem": "A bank account has a balance of -$50 (overdrawn). You deposit $75. What is the new balance?", "answer": "$25"}
            ],
            "proficient": [
                {"problem": "Calculate: -3 + (-5) - 2 + 6. Show each step.", "answer": "-3 - 5 - 2 + 6 = -8 - 2 + 6 = -10 + 6 = -4"},
                {"problem": "On a winter day, the high temperature is -2°F and the low is -15°F. What is the temperature difference?", "answer": "13°F"},
                {"problem": "A golf player's scores relative to par for 4 rounds are: -1, +2, -3, +1. What is their total score relative to par?", "answer": "-1 (one under par)"}
            ],
            "extending": [
                {"problem": "An elevator starts on floor 5. It goes down 7 floors, then up 3 floors, then down 2 floors. Where does it end? Write an equation that represents this journey and explain what each number represents.", "answer": "5 - 7 + 3 - 2 = -1 (one floor below ground). Positive numbers = going up, negative = going down."},
                {"problem": "If the sum of two numbers is -10 and one number is 3, what is the other number? Verify using addition.", "answer": "-13. Check: 3 + (-13) = -10. ✓"},
                {"problem": "Explain why -5 + 5 = 0 using a real-world context (like money, temperature, or movement). Why is this relationship important?", "answer": "Example: If you gain $5 and lose $5, your net change is $0. These are opposites/additive inverses. This is important because it shows that opposite quantities cancel out and helps us understand zero as a reference point."}
            ]
        }
    },
    "absolute value": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "What is the absolute value of -5? Write: |-5| = ?", "answer": "5"},
                {"problem": "What is |7|?", "answer": "7"},
                {"problem": "A diver is 12 meters below the surface. What is the absolute value of their depth?", "answer": "12"}
            ],
            "developing": [
                {"problem": "Calculate: |-8| + |3|", "answer": "11"},
                {"problem": "Which is greater: |-9| or |4|?", "answer": "|-9| because |-9| = 9 and |4| = 4, and 9 > 4"},
                {"problem": "The temperature dropped 6 degrees from the morning. Write the change as a negative integer and find its absolute value.", "answer": "-6; |-6| = 6"}
            ],
            "proficient": [
                {"problem": "Solve: |x| = 7. What are all possible values of x?", "answer": "x = 7 or x = -7"},
                {"problem": "Two students are at different positions on a number line: Student A is at -4 and Student B is at 3. What is the distance between them?", "answer": "|3 - (-4)| = |7| = 7 units"},
                {"problem": "Calculate: |-5| - |2| + |-3|. Show your work.", "answer": "5 - 2 + 3 = 6"}
            ],
            "extending": [
                {"problem": "A city is 8 miles west of a reference point, and another city is 6 miles east. Use absolute value to represent each location and calculate the distance between them. Explain what the absolute value tells us in this context.", "answer": "West city: -8; East city: +6. Distance = |-8 - 6| = |-14| = 14 miles. Absolute value gives us the distance magnitude regardless of direction."},
                {"problem": "If |x - 5| = 3, what are the possible values of x? Show how you solved this algebraically.", "answer": "x - 5 = 3 or x - 5 = -3. So x = 8 or x = 2. The absolute value represents a distance of 3 units from 5."},
                {"problem": "Explain why |a| = |-a| for any number a. Use at least two examples to support your explanation.", "answer": "Because absolute value measures distance from zero, which is always positive. Examples: |3| = |-3| = 3 (both are 3 units from zero); |-7| = |7| = 7 (both are 7 units from zero). Distance doesn't depend on direction."}
            ]
        }
    },
    "variables and expressions": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "If n = 5, what is the value of n + 3?", "answer": "8"},
                {"problem": "Write an expression for 'a number times 2'. Use x for the number.", "answer": "2x or x × 2"},
                {"problem": "If s = 4, find the value of 3s.", "answer": "12"}
            ],
            "developing": [
                {"problem": "If a = 6 and b = 2, find the value of 2a + b.", "answer": "14"},
                {"problem": "Write an expression for 'the cost of a ticket is $8 more than the program cost'. Let p = program cost.", "answer": "p + 8"},
                {"problem": "Simplify: 3x + 2x", "answer": "5x"}
            ],
            "proficient": [
                {"problem": "If x = 4, evaluate: 2x² + 3x - 5. Show each step.", "answer": "2(16) + 3(4) - 5 = 32 + 12 - 5 = 39"},
                {"problem": "Write an expression for: 'You have twice as many apples as oranges, and 5 fewer bananas than apples.' Let o = number of oranges.", "answer": "2o apples; 2o - 5 bananas"},
                {"problem": "Simplify: 4a + 2b - a + 3b", "answer": "3a + 5b"}
            ],
            "extending": [
                {"problem": "A phone company charges $25 per month plus $0.10 per text message. Write an expression for the total monthly cost if you send t text messages. If you send 150 text messages, what is your bill? Explain what each part of your expression represents.", "answer": "25 + 0.10t. Cost = 25 + 0.10(150) = 25 + 15 = $40. The 25 is the fixed fee, 0.10t is the variable cost based on texts."},
                {"problem": "If the area of a rectangle is A = lw and the length is 3 more than twice the width, write an expression for area in terms of width w only. Simplify.", "answer": "A = (2w + 3)(w) = 2w² + 3w"},
                {"problem": "Explain why 2x + 3x simplifies to 5x, but 2x + 3y does not simplify further. Use the concept of like terms to justify your answer.", "answer": "2x and 3x are like terms (same variable, same power), so their coefficients combine: 2 + 3 = 5. But 2x and 3y have different variables, so they cannot be combined. Like terms must have identical variable parts."}
            ]
        }
    },
    "one-step equations": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "Solve: x + 4 = 9", "answer": "x = 5"},
                {"problem": "Solve: 3x = 12", "answer": "x = 4"},
                {"problem": "Solve: x - 2 = 7", "answer": "x = 9"}
            ],
            "developing": [
                {"problem": "Solve: x/5 = 3. Check your answer.", "answer": "x = 15. Check: 15/5 = 3 ✓"},
                {"problem": "A number increased by 8 is 15. Write and solve an equation.", "answer": "x + 8 = 15; x = 7"},
                {"problem": "Solve: 2x = 14", "answer": "x = 7"}
            ],
            "proficient": [
                {"problem": "Solve: 4x - 3 = 13... Wait, this is two-step. Let me revise. Solve: 6 + x = -2", "answer": "x = -8"},
                {"problem": "A video game costs $5 less than a board game. If the video game costs $12, what is the cost of the board game? Write and solve.", "answer": "x - 5 = 12; x = $17"},
                {"problem": "Solve and verify: x/2 = 6", "answer": "x = 12. Verify: 12/2 = 6 ✓"}
            ],
            "extending": [
                {"problem": "A student has some money. After spending $8, they have $15 left. Write an equation and solve. Explain what the variable represents and verify your answer makes sense in context.", "answer": "x - 8 = 15; x = $23. The variable represents the original amount. Check: $23 - $8 = $15 ✓. This makes sense because you need more than $15 originally to have $15 left after spending."},
                {"problem": "Create a one-step equation that has x = -4 as its solution. Explain your thinking.", "answer": "Example: x + 6 = 2 (or x - 3 = -7, or 2x = -8, etc.). One approach: I want x to equal -4, so I could add 6 to it and get 2. So my equation is x + 6 = 2."},
                {"problem": "Explain why solving x + 5 = 12 and solving 5 + x = 12 give the same answer, even though the equations look different. What property allows this?", "answer": "Both equal x = 7 because of the Commutative Property of Addition, which states that a + b = b + a. The order doesn't matter; we're still isolating x the same way."}
            ]
        }
    },
    "area of polygons": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "A rectangle has length 5 cm and width 3 cm. What is the area?", "answer": "15 cm²"},
                {"problem": "Find the area of a square with side length 4 inches.", "answer": "16 in²"},
                {"problem": "A triangle has a base of 6 cm and height of 4 cm. What is its area?", "answer": "12 cm²"}
            ],
            "developing": [
                {"problem": "A parallelogram has base 8 m and height 5 m. What is the area?", "answer": "40 m²"},
                {"problem": "A trapezoid has parallel sides of 5 cm and 7 cm, with height 4 cm. Find the area.", "answer": "24 cm²"},
                {"problem": "A rectangle has area 24 square feet and length 6 feet. What is the width?", "answer": "4 feet"}
            ],
            "proficient": [
                {"problem": "A triangle has an area of 30 cm² and a height of 5 cm. What is the length of the base?", "answer": "12 cm"},
                {"problem": "A garden in the shape of a trapezoid has bases of 10 m and 6 m with height 8 m. What is the area? If you want to fence the perimeter and fencing costs $5 per meter, what additional information would you need?", "answer": "Area = 64 m². You would need the lengths of the non-parallel sides to calculate perimeter."},
                {"problem": "Find the total area of a composite figure made of a rectangle (8 × 6) and a triangle on top (base 8, height 3).", "answer": "48 + 12 = 60 square units"}
            ],
            "extending": [
                {"problem": "A property is shaped like a pentagon that can be divided into a rectangle and a triangle. The rectangle is 20 ft × 15 ft, and the triangle on top has a base of 20 ft and height of 8 ft. Find the total area. Draw and label a diagram of your thinking.", "answer": "Rectangle: 20 × 15 = 300 sq ft. Triangle: (20 × 8)/2 = 80 sq ft. Total: 380 sq ft. (Diagram should show rectangle with triangle on top, with all dimensions labeled)"},
                {"problem": "If you double all the dimensions of a polygon, what happens to the area? Test this with a rectangle of 4 × 6 and explain why this relationship exists.", "answer": "Original: 4 × 6 = 24. Doubled: 8 × 12 = 96. The area quadruples (24 × 4 = 96). This happens because both length and width double, so area = (2l)(2w) = 4lw."},
                {"problem": "A triangle with base 10 cm has area 35 cm². A similar triangle has base 15 cm. What is the area of the second triangle? Explain your reasoning.", "answer": "Base increased by a factor of 1.5 (15/10 = 1.5). Since the triangles are similar, height also increases by 1.5. Area increases by 1.5² = 2.25. New area: 35 × 2.25 = 78.75 cm². (Or: new height is 7 × 1.5 = 10.5; area = 0.5 × 15 × 10.5 = 78.75)"}
            ]
        }
    },
    "surface area and volume": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "A rectangular prism has length 4 cm, width 3 cm, and height 2 cm. What is the volume?", "answer": "24 cm³"},
                {"problem": "A cube has side length 3 inches. What is its volume?", "answer": "27 in³"},
                {"problem": "A box is 5 m long, 3 m wide, and 2 m tall. What is the volume?", "answer": "30 m³"}
            ],
            "developing": [
                {"problem": "Find the surface area of a cube with side length 2 cm. (Hint: A cube has 6 faces)", "answer": "24 cm² (6 × 2² = 6 × 4)"},
                {"problem": "A rectangular prism has length 5 cm, width 4 cm, and height 3 cm. Find the surface area.", "answer": "94 cm² (2(5×4) + 2(5×3) + 2(4×3) = 40 + 30 + 24)"},
                {"problem": "A cylinder has radius 2 cm and height 5 cm. What is the volume? Use π ≈ 3.14", "answer": "62.8 cm³ (πr²h ≈ 3.14 × 4 × 5)"}
            ],
            "proficient": [
                {"problem": "A rectangular prism has surface area 100 cm². If length is 5 cm and width is 4 cm, what is the height? Show your work.", "answer": "Using SA = 2(lw + lh + wh): 100 = 2(20 + 5h + 4h); 100 = 2(20 + 9h); 50 = 20 + 9h; h = 30/9 = 3⅓ cm"},
                {"problem": "Find the total surface area of a rectangular prism with dimensions 6 cm × 4 cm × 3 cm, then verify your answer using the formula SA = 2(lw + lh + wh).", "answer": "2(6×4 + 6×3 + 4×3) = 2(24 + 18 + 12) = 2(54) = 108 cm²"},
                {"problem": "A storage container in the shape of a rectangular prism has dimensions 10 ft × 8 ft × 6 ft. What is the volume, and if one cubic foot holds 62.5 pounds of material, how much can the container hold?", "answer": "Volume = 480 cubic feet. Capacity = 480 × 62.5 = 30,000 pounds"}
            ],
            "extending": [
                {"problem": "You need to wrap a gift in a rectangular box with dimensions 12 in × 8 in × 5 in. The wrapping paper costs $0.02 per square inch. Find the surface area and calculate the cost. What assumptions are you making about waste?", "answer": "SA = 2(12×8 + 12×5 + 8×5) = 2(96 + 60 + 40) = 392 sq in. Cost ≈ $7.84. Assumes no waste; real wrapping would cost more due to overlaps and trimming."},
                {"problem": "A rectangular prism has volume 120 cm³. If you want a prism with double the volume, how should you change the dimensions? Explain whether you could keep all dimensions the same or need to change some.", "answer": "You could double one dimension (length × 2, width, height), or scale all three dimensions by ∛2 ≈ 1.26. Doubling one dimension gives exactly double the volume. Scaling all dimensions by factor k changes volume by k³."},
                {"problem": "Two rectangular prisms have the same volume of 60 m³. One has dimensions 5 × 4 × 3. Find dimensions for another prism with the same volume that has a different shape. Which has greater surface area? Explain why volume alone doesn't determine surface area.", "answer": "Example: 10 × 2 × 3 (SA = 112 m²) vs 5 × 4 × 3 (SA = 94 m²). The 10 × 2 × 3 has greater SA. Volume measures 3D space; surface area measures outer coverage. Different shapes can enclose same volume but need different amounts of material."}
            ]
        }
    },
    "statistical distributions": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "Create a dot plot for this data: 2, 3, 3, 4, 4, 4, 5. What value appears most often?", "answer": "4 appears most often (mode = 4)"},
                {"problem": "Make a bar graph with these categories: Apples (5), Oranges (3), Bananas (6), Grapes (4). What is the most popular fruit?", "answer": "Bananas (6)"},
                {"problem": "Heights of students: 60, 62, 64, 65, 65, 66, 68 inches. What is the range?", "answer": "8 inches (68 - 60)"}
            ],
            "developing": [
                {"problem": "Create a histogram for test scores: 70, 72, 75, 78, 80, 82, 85, 88, 90, 92. Use bins of 10 (70-79, 80-89, 90-99). Which bin has the most scores?", "answer": "70-79 bin has 4 scores; 80-89 has 4 scores; 90-99 has 2 scores. (70-79 and 80-89 tie)"},
                {"problem": "A survey asked people their favorite color. Results: Blue (12), Red (8), Green (10), Yellow (5). Draw a bar graph and describe the distribution.", "answer": "Bar graph shows Blue highest, then Green, then Red, then Yellow. Distribution shows most prefer blue, least prefer yellow."},
                {"problem": "The weights of puppies are: 3, 4, 4, 5, 5, 5, 6, 7, 8 pounds. Describe the shape of the distribution.", "answer": "The distribution is somewhat symmetric with a peak around 5 pounds, showing that most puppies weigh around 5 pounds."}
            ],
            "proficient": [
                {"problem": "A class of 20 students took a quiz. Scores: 65, 70, 72, 75, 76, 78, 80, 82, 82, 85, 85, 85, 88, 90, 90, 92, 92, 95, 98, 100. Create a frequency table with intervals (60-70, 71-80, 81-90, 91-100) and describe the distribution.", "answer": "60-70: 2; 71-80: 5; 81-90: 8; 91-100: 5. Distribution is roughly symmetric, centered around the 81-90 interval, suggesting most students performed in the B-A range."},
                {"problem": "Two classes took the same test. Class A: mean = 82, range = 30. Class B: mean = 80, range = 10. What does this tell you about the distributions?", "answer": "Both classes have similar average performance, but Class A has much more variability (wider spread) while Class B is more consistent. Class B students' scores are clustered closer together."},
                {"problem": "Create a box plot for: 12, 15, 18, 20, 22, 24, 25, 26, 28, 30. Identify the minimum, Q1, median, Q3, and maximum.", "answer": "Min = 12, Q1 = 18, Median = 23, Q3 = 26, Max = 30"}
            ],
            "extending": [
                {"problem": "You have two datasets representing test scores from two different teaching methods. Dataset A: 70, 72, 75, 78, 80, 82, 85, 88, 90 (mean ≈ 80, std dev ≈ 6.6). Dataset B: 60, 65, 75, 85, 90, 90, 95, 95, 100 (mean ≈ 84.4, std dev ≈ 12.1). Which method might be better? Why might you use different measures (mean, median, range, standard deviation) to compare these distributions?", "answer": "Method A has lower mean but more consistent results (low std dev). Method B has higher mean but more variable results (high std dev). Choice depends on goals: Method A for reliability/consistency, Method B for high achievers but wider gaps. Different measures reveal different aspects: mean shows average, std dev shows consistency, median shows typical value resistant to outliers."},
                {"problem": "A restaurant tracks customer satisfaction scores monthly. Describe what a right-skewed distribution and a left-skewed distribution would mean in this context. Which would indicate better business?", "answer": "Right-skewed (tail to right): tail of low scores, most ratings high. Left-skewed (tail to left): tail of high scores, most ratings low. Right-skewed is better—most customers satisfied, few complaints. In distributions, skewness shows direction of unusual values and affects relationship between mean and median."},
                {"problem": "Explain why the same dataset could have very different appearances depending on the bin size in a histogram. Create an example using the same 20 data points with two different bin sizes and describe how the visual interpretation changes.", "answer": "Small bins (width 2) show more detail and variation; large bins (width 5) smooth out variation and show overall pattern. Example: Data 20-30: small bins might appear multimodal, large bins show roughly uniform distribution. Bin size selection affects whether we see noise (small bins) or pattern (large bins). Choosing appropriate bin size is important for accurate data representation."}
            ]
        }
    },
    "measures of center": {
        "grade": 6,
        "levels": {
            "entry": [
                {"problem": "Find the mean of: 2, 4, 6, 8", "answer": "5"},
                {"problem": "Find the median of: 3, 5, 7, 9, 11", "answer": "7"},
                {"problem": "Find the mode of: 1, 2, 2, 3, 2, 4", "answer": "2"}
            ],
            "developing": [
                {"problem": "Test scores: 75, 80, 85, 90, 95. Find the mean, median, and mode.", "answer": "Mean = 85, Median = 85, Mode = none (no repeating values)"},
                {"problem": "Heights of players: 5'10\", 5'11\", 5'11\", 6'0\", 6'2\". What is the median height?", "answer": "5'11\" (middle value)"},
                {"problem": "Prices of books: $8, $10, $12, $15, $100. Which measure of center best represents typical price? Why?", "answer": "Median ($12) is better than mean ($29) because the $100 book is an outlier that pulls the mean up"}
            ],
            "proficient": [
                {"problem": "A student's quiz scores are 78, 82, 85, 92, 88. What is the mean score?", "answer": "425/5 = 85"},
                {"problem": "Data set: 4, 6, 8, 9, 10, 15. Find the mean, median, and range. Explain how the outlier (15) affects the mean.", "answer": "Mean = 52/6 ≈ 8.67. Median = (8+9)/2 = 8.5. Range = 11. The 15 pulls the mean up; median is more resistant to this outlier."},
                {"problem": "Sales data for a week: Mon $150, Tue $140, Wed $165, Thu $160, Fri $175, Sat $200, Sun $180. Find the mean daily sales.", "answer": "Sum = $1170; Mean = $1170/7 ≈ $167.14"}
            ],
            "extending": [
                {"problem": "A company has 10 employees with salaries: $30k, $32k, $35k, $38k, $40k, $42k, $45k, $48k, $50k, $150k. Calculate mean, median, and mode. The owner claims 'our average salary is high.' Is this misleading? Explain which measure best represents typical employee salary.", "answer": "Mean = $65.2k, Median = $41k, Mode = none. Yes, it's misleading—mean is inflated by the $150k salary. Median ($41k) better represents typical salary since the $150k is an outlier. Using mean when median is more appropriate is a common statistical misuse."},
                {"problem": "Two classes have the same mean test score of 80. Class A scores: 75, 78, 80, 82, 85. Class B scores: 60, 70, 80, 90, 100. Why might the teacher be concerned about Class B despite equal means? What additional statistics would be helpful?", "answer": "Class A is consistent; Class B has huge spread (range 40 vs 10). Dispersion measures like range, interquartile range, or standard deviation would reveal that Class B's scores vary much more. Equal means hide very different distributions."},
                {"problem": "If a dataset has mean 75 and you add a new data point of 75, does the mean change? What if you add 100? Explain the mathematical reason why.", "answer": "Adding 75: mean stays 75 (new point equals current mean). Adding 100: mean increases (new point above current mean pulls it up). Mathematically: new mean = (old sum + new value)/(n+1). If new value > old mean, new mean increases; if new value < old mean, new mean decreases."}
            ]
        }
    },
    "proportional relationships": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "If y = 2x, fill in the table: x = 1, y = ?; x = 2, y = ?; x = 3, y = ?", "answer": "y = 2, 4, 6"},
                {"problem": "Is this a proportional relationship? x: 1, 2, 3 and y: 3, 6, 9. Explain.", "answer": "Yes, because y/x = 3 for all pairs (constant ratio)"},
                {"problem": "A recipe calls for 2 cups of flour per 1 cup of sugar. How much flour for 3 cups of sugar?", "answer": "6 cups of flour"}
            ],
            "developing": [
                {"problem": "Create a table for the proportional relationship y = 3x. Plot at least 4 points on a coordinate plane.", "answer": "Table: (0,0), (1,3), (2,6), (3,9). All points lie on a straight line through the origin."},
                {"problem": "Which equation represents a proportional relationship? A) y = 2x + 1  B) y = 2x  C) y = x²", "answer": "B) y = 2x (proportional relationships have form y = kx and pass through origin)"},
                {"problem": "If a car travels 60 miles in 2 hours at constant speed, how far does it travel in 5 hours?", "answer": "150 miles (rate = 30 mph; 30 × 5 = 150)"}
            ],
            "proficient": [
                {"problem": "A printer prints 120 pages in 2 minutes. Make a graph of the relationship between time (x) and pages (y). Write the equation and find how many pages print in 7 minutes.", "answer": "Equation: y = 60x. At 7 minutes: y = 420 pages. Graph shows straight line through origin with points like (1,60), (2,120), (3,180)."},
                {"problem": "Two recipes are in proportion. Recipe A: 3 cups flour, 2 cups sugar. Recipe B: x cups flour, 5 cups sugar. Find x.", "answer": "3/2 = x/5; x = 7.5 cups"},
                {"problem": "Is the relationship between gallons and liters proportional? (1 gallon = 3.785 liters, 2 gallons = 7.57 liters, 5 gallons = 18.925 liters). Explain.", "answer": "Yes, the constant of proportionality k ≈ 3.785 (liters per gallon) is consistent for all values."}
            ],
            "extending": [
                {"problem": "A phone plan charges $40/month plus $0.10 per text message. Is cost proportional to the number of texts? Why or why not? How would the relationship change if there were no base fee? Graph both scenarios.", "answer": "No, the $40 base fee breaks proportionality (not y = kx form). Without the base fee (just $0.10/text), it would be proportional. Key: proportional relationships have no constant added; they pass through origin."},
                {"problem": "The ratio of boys to girls in a school is 4:5. If there are 180 boys, how many girls are there? Write and solve a proportion. Then explain what would happen to this ratio if 20 new girls enrolled.", "answer": "4/5 = 180/g; g = 225 girls. If 20 girls enroll: new ratio = 180:(225+20) = 180:245 ≈ 4:5.4, slightly less boys-to-girls."},
                {"problem": "Two quantities are inversely proportional: as one increases, the other decreases proportionally (xy = k). Give a real-world example and explain why it's not a standard proportional relationship (y = kx). When might inverse proportionality be more useful?", "answer": "Example: speed and time for fixed distance (faster speed = less time; speed × time = distance). Not y=kx form because when x increases, y decreases. Useful for: work rates, concentration and volume, pressure and volume. This models situations where a product is constant, not a quotient."}
            ]
        }
    },
    "operations with rational numbers": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "Calculate: 0.5 + 0.3", "answer": "0.8"},
                {"problem": "Calculate: 1/2 + 1/4", "answer": "3/4"},
                {"problem": "Calculate: 0.6 - 0.2", "answer": "0.4"}
            ],
            "developing": [
                {"problem": "Calculate: 2/3 + 1/6. Simplify.", "answer": "5/6"},
                {"problem": "Calculate: 0.75 × 0.8", "answer": "0.6"},
                {"problem": "Calculate: 5/8 - 1/4", "answer": "3/8"}
            ],
            "proficient": [
                {"problem": "Calculate: -2/3 + 5/6. Show your work.", "answer": "-4/6 + 5/6 = 1/6"},
                {"problem": "Calculate: 3.5 + (-1.2) - 2.8. Show each step.", "answer": "3.5 - 1.2 - 2.8 = 2.3 - 2.8 = -0.5"},
                {"problem": "Calculate: (2/3) × (-3/4) ÷ (1/2)", "answer": "(2/3 × (-3/4)) ÷ (1/2) = (-1/2) ÷ (1/2) = -1"}
            ],
            "extending": [
                {"problem": "A recipe calls for 1 3/4 cups of flour. If you make 2 1/3 batches, how much flour do you need? Express your answer as a mixed number and explain your steps.", "answer": "1 3/4 × 2 1/3 = 7/4 × 7/3 = 49/12 = 4 1/12 cups. Convert to mixed numbers, multiply fractions, simplify."},
                {"problem": "A student scores 0.85 on one exam and 0.92 on another. What is the average score? If the final exam counts twice as much, and they score 0.88, what is the weighted average? (Weighted average = sum of (score × weight) / total weight)", "answer": "Simple average: (0.85 + 0.92)/2 = 0.885. Weighted average: (0.85 + 0.92 + 0.88 × 2)/(1+1+2) = 3.53/4 = 0.8825."},
                {"problem": "Explain why (-3/4) × (-2/5) equals 6/20 = 3/10. Use the rule about negative signs in multiplication and verify by finding the reciprocal relationship. Why do two negatives make a positive?", "answer": "Negative × negative = positive (opposite of opposite returns to positive). (-3/4) × (-2/5) = (3/4) × (2/5) = 6/20 = 3/10. This reflects the mathematical principle that negating a quantity twice returns it to its original sign."}
            ]
        }
    },
    "expressions and equivalent forms": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "Simplify: 3x + 2x", "answer": "5x"},
                {"problem": "Simplify: 4(x + 2)", "answer": "4x + 8"},
                {"problem": "Are 2(x + 3) and 2x + 6 equivalent? Explain.", "answer": "Yes, they're equivalent by the distributive property"}
            ],
            "developing": [
                {"problem": "Simplify: 2x + 3y + 5x - y", "answer": "7x + 2y"},
                {"problem": "Factor: 6x + 9", "answer": "3(2x + 3)"},
                {"problem": "Expand: 3(2x - 4)", "answer": "6x - 12"}
            ],
            "proficient": [
                {"problem": "Show that 2(x + 4) - 3 and 2x + 5 are equivalent by expanding and simplifying.", "answer": "2(x + 4) - 3 = 2x + 8 - 3 = 2x + 5 ✓"},
                {"problem": "Factor completely: 4x² + 8x", "answer": "4x(x + 2)"},
                {"problem": "Simplify: 5(2x + 3) - 2(x - 4)", "answer": "10x + 15 - 2x + 8 = 8x + 23"}
            ],
            "extending": [
                {"problem": "Prove that n(n+1) and n² + n are equivalent expressions. Then use this to find a shortcut for multiplying any number by its successor (e.g., 7 × 8). Explain why this works.", "answer": "n(n+1) = n² + n (distribute). Example: 7 × 8 = 7² + 7 = 49 + 7 = 56. Works because multiplying a number by (itself + 1) is the same as the number squared plus the number itself."},
                {"problem": "The area of a rectangle is represented by 3x(2x + 5). Write at least two equivalent forms. Explain what each form tells you about the rectangle.", "answer": "6x² + 15x (standard form: shows total area). 3x(2x + 5) (factored form: shows length 3x and width (2x+5)). 3(2x² + 5x) (different factorization). Each reveals different information about dimensions."},
                {"problem": "If a student claims that a² + b² = (a+b)², show this is false with a counterexample. Then write the correct expansion of (a+b)² and explain where the student's mistake comes from. Why is this a common error?", "answer": "Counterexample: 3² + 4² = 9 + 16 = 25, but (3+4)² = 49. Correct: (a+b)² = a² + 2ab + b². Error comes from ignoring the middle term 2ab. Students often assume operations distribute when they don't (squaring does not distribute over addition)."}
            ]
        }
    },
    "two-step equations": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "Solve: 2x + 3 = 7", "answer": "x = 2"},
                {"problem": "Solve: 3x - 5 = 10", "answer": "x = 5"},
                {"problem": "Solve: x/2 + 4 = 8", "answer": "x = 8"}
            ],
            "developing": [
                {"problem": "Solve: 4x - 7 = 9. Check your answer.", "answer": "x = 4. Check: 4(4) - 7 = 16 - 7 = 9 ✓"},
                {"problem": "Solve: (x - 3)/5 = 2", "answer": "x = 13"},
                {"problem": "Twice a number minus 6 equals 14. Find the number.", "answer": "2x - 6 = 14; x = 10"}
            ],
            "proficient": [
                {"problem": "Solve: 3(x + 2) = 18. Show each step.", "answer": "3x + 6 = 18; 3x = 12; x = 4"},
                {"problem": "Solve for x: -2x + 5 = -7. Verify your solution.", "answer": "-2x = -12; x = 6. Check: -2(6) + 5 = -12 + 5 = -7 ✓"},
                {"problem": "A phone costs $20 less than a tablet. Together they cost $280. Write and solve an equation to find each price.", "answer": "Let t = tablet cost. t + (t - 20) = 280; 2t - 20 = 280; 2t = 300; t = $150 (tablet), phone = $130"}
            ],
            "extending": [
                {"problem": "Solve the equation 2(x - 3) + 5 = 4x - 7. Explain each step. Then create a real-world problem that would require this equation to solve.", "answer": "2x - 6 + 5 = 4x - 7; 2x - 1 = 4x - 7; -2x = -6; x = 3. Example: 'Two phone plans: Plan A costs $2 per song minus $3 setup credit plus $5 bonus. Plan B costs $4 per song minus $7 credit. When are they equal?'"},
                {"problem": "If 3x + 5 = 2x + 10 and 2x + 10 = 20, solve for x using both equations. Explain why solving either one gives the same answer.", "answer": "From equation 1: x = 5. From equation 2: x = 5. Both work because if a = b and b = c, then a = c (transitivity). Equations are linked."},
                {"problem": "Explain why the equation 2x + 3 = 2x + 5 has no solution. What does this mean graphically? When would you encounter an equation with no solution in a real situation?", "answer": "Subtracting 2x: 3 = 5 (impossible). Graphically, the two sides represent parallel lines (same slope, different y-intercepts) that never intersect. Real example: 'I earn $2/hour plus $3 bonus, you earn $2/hour plus $5 bonus. When do we earn the same amount?' Never—you always earn $2 more."}
            ]
        }
    },
    "scale drawings": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "A map has scale 1 inch : 10 miles. If two cities are 2 inches apart on the map, how far apart are they in reality?", "answer": "20 miles"},
                {"problem": "A drawing has scale 1 : 50. If something is 2 units on the drawing, how long is it in reality?", "answer": "100 units"},
                {"problem": "A model car is 6 inches long. The scale is 1 : 24. How long is the real car?", "answer": "144 inches or 12 feet"}
            ],
            "developing": [
                {"problem": "A room is 12 feet by 15 feet. On a scale drawing with scale 1/4 inch : 1 foot, what are the dimensions on the drawing?", "answer": "3 inches by 3.75 inches"},
                {"problem": "An architectural drawing uses scale 1 : 100. A wall measures 5 cm on the drawing. What is the actual length?", "answer": "500 cm or 5 meters"},
                {"problem": "A playground is 60 feet long. On a map with scale 1 inch : 30 feet, how many inches long is it on the map?", "answer": "2 inches"}
            ],
            "proficient": [
                {"problem": "A building is 80 feet tall. On a scale drawing with scale 1 inch : 10 feet, how tall is the building on the drawing? If the drawing width is 3 inches, what is the actual width?", "answer": "Height on drawing: 8 inches. Actual width: 3 × 10 = 30 feet"},
                {"problem": "Two map scales are available: 1 : 500 and 1 : 1000. For a 500-meter distance, calculate the map distance for each scale. Which scale gives a larger drawing?", "answer": "1:500 scale: 500m ÷ 500 = 1m = 100 cm. 1:1000 scale: 500m ÷ 1000 = 0.5m = 50 cm. The 1:500 scale gives larger drawing."},
                {"problem": "A rectangular garden measures 30 ft × 40 ft. Make a scale drawing using scale 1/2 inch : 5 feet. What are the drawing dimensions? What is the area of the drawing?", "answer": "Drawing dimensions: 3 inches × 4 inches. Drawing area: 12 sq inches. (Real area: 1200 sq ft)"}
            ],
            "extending": [
                {"problem": "A city block is 250 feet × 300 feet. Create a scale drawing for a neighborhood map (multiple blocks). Choose an appropriate scale and explain your reasoning. If you wanted to show more blocks but fit the same paper size, how would you change the scale? Describe the trade-offs.", "answer": "Example: Scale 1/8 inch : 50 feet gives 5 in × 6 in (good size). To fit more blocks: use smaller scale like 1/16 inch : 50 feet (gives 2.5 × 3 in—shows more blocks but less detail). Trade-off: larger scale = more detail but fewer blocks; smaller scale = more coverage but less detail."},
                {"problem": "An architect is designing a house. The actual house will be 45 feet long. If the architectural drawing uses scale 1/4 inch : 3 feet, what is the length on the drawing? If a wall is measured as 1.5 inches on the drawing, what is its actual length?", "answer": "House length on drawing: 45 ÷ 3 × 1/4 = 3.75 inches. Wall actual length: 1.5 ÷ (1/4) × 3 = 1.5 × 4 × 3 = 18 feet."},
                {"problem": "Explain why the area of a scale drawing is NOT the actual area multiplied by the scale factor. If a scale is 1 : 10, how does the area on the drawing compare to the actual area? Use an example with specific measurements.", "answer": "A 1:10 scale means linear dimensions are 1/10; areas are (1/10)² = 1/100 of actual. Example: 100 sq ft room drawn at 1:10 scale has 100 × (1/10)² = 1 sq ft on drawing. Scale factor applies twice for area because area is 2-dimensional. This is why (scale factor)² determines area ratios."}
            ]
        }
    },
    "circumference and area": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "Find the circumference of a circle with radius 5 cm. Use π ≈ 3.14", "answer": "C = 2πr ≈ 2 × 3.14 × 5 ≈ 31.4 cm"},
                {"problem": "Find the area of a circle with radius 3 inches. Use π ≈ 3.14", "answer": "A = πr² ≈ 3.14 × 9 ≈ 28.26 sq in"},
                {"problem": "A circle has diameter 10 meters. What is its circumference?", "answer": "C = πd ≈ 3.14 × 10 ≈ 31.4 m"}
            ],
            "developing": [
                {"problem": "Find circumference and area of a circle with radius 7 cm. Use π ≈ 22/7", "answer": "C = 2 × (22/7) × 7 = 44 cm. A = (22/7) × 49 = 154 cm²"},
                {"problem": "A pizza has diameter 12 inches. What is the circumference?", "answer": "C = π × 12 ≈ 37.7 inches"},
                {"problem": "A circular track has circumference 400 meters. What is the radius?", "answer": "C = 2πr; 400 = 2πr; r ≈ 63.66 meters"}
            ],
            "proficient": [
                {"problem": "A circle has area 50 cm². Find the radius and circumference. Show work.", "answer": "A = πr²; 50 = 3.14r²; r² ≈ 15.92; r ≈ 3.99 cm. C ≈ 2 × 3.14 × 3.99 ≈ 25.06 cm"},
                {"problem": "Two circles: Circle A has radius 4 m, Circle B has radius 8 m. Compare their circumferences and areas. What is the relationship?", "answer": "Circle A: C ≈ 25.12 m, A ≈ 50.24 m². Circle B: C ≈ 50.24 m, A ≈ 201 m². Circumference doubles (scale factor 2). Area quadruples (scale factor 4 = 2²)."},
                {"problem": "A fountain is circular with radius 6 feet. A decorator needs to place lights every 2 feet around the circumference. How many lights are needed?", "answer": "C = 2π(6) ≈ 37.7 feet. Number of lights: 37.7 ÷ 2 ≈ 19 lights (or 18-20 depending on rounding)"}
            ],
            "extending": [
                {"problem": "A circular garden has area 100 m². You want to install edging around it. The edging costs $8 per meter. Calculate the circumference and total cost. Explain how knowing the area allows you to find the circumference.", "answer": "A = πr²; 100 = πr²; r ≈ 5.64 m. C = 2πr ≈ 35.45 m. Cost ≈ $283.60. We find radius from area (r = √(A/π)), then use radius to find circumference."},
                {"problem": "A circular trampoline has circumference 44 feet. Find its area. A company makes covers that cost $0.50 per square foot. What is the cost of a cover?", "answer": "C = 44 ft; 44 = 2πr; r ≈ 7 ft. A = πr² ≈ 154 sq ft. Cost ≈ $77."},
                {"problem": "Explain why multiplying the radius by 3 multiplies the area by 9, not by 3. Use both formulas and explain how this relates to the difference between linear and quadratic relationships.", "answer": "A = πr². If r becomes 3r: A' = π(3r)² = π × 9r² = 9πr² = 9A. The area multiplies by 3² = 9 because area involves r squared. Linear measurements scale by factor k; areas scale by k²; volumes scale by k³. This is why doubling all dimensions increases area 4 times."}
            ]
        }
    },
    "angle relationships": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "Two angles are complementary. One is 30°. What is the other?", "answer": "60°"},
                {"problem": "Two angles are supplementary. One is 120°. What is the other?", "answer": "60°"},
                {"problem": "At an intersection, two lines form vertical angles. One angle is 45°. What is the vertical angle?", "answer": "45°"}
            ],
            "developing": [
                {"problem": "Two parallel lines are cut by a transversal. A corresponding angle on the first line is 75°. What is the corresponding angle on the second line?", "answer": "75°"},
                {"problem": "Find the missing angle in a triangle: Two angles are 50° and 70°. What is the third?", "answer": "60° (sum must be 180°)"},
                {"problem": "At a point, several angles are formed. Two adjacent angles are 40° and 50°. What is the angle formed by going all the way around (360°)?", "answer": "The remaining angle is 360° - 40° - 50° = 270° (or three angles form 360°)"}
            ],
            "proficient": [
                {"problem": "Two parallel lines cut by a transversal form angles. If an alternate interior angle is 65°, what is the corresponding angle on the parallel line?", "answer": "65° (alternate interior angles are equal when lines are parallel)"},
                {"problem": "In a triangle, one angle is twice another, and the third is 30°. Find all three angles.", "answer": "Let x = first angle, 2x = second. x + 2x + 30 = 180; 3x = 150; x = 50°. Angles: 50°, 100°, 30°"},
                {"problem": "Two supplementary angles have measures (3x) and (x + 20). Find both angles.", "answer": "3x + (x + 20) = 180; 4x + 20 = 180; 4x = 160; x = 40. Angles are 120° and 60°."}
            ],
            "extending": [
                {"problem": "Two parallel lines are cut by a transversal. Name all 8 angles formed and explain which angles are equal and why. If one angle is 50°, find all others.", "answer": "8 angles at two intersections. Corresponding angles equal (both 50° or 130°). Alternate interior/exterior equal. Vertical angles equal. Adjacent angles supplementary. 4 angles = 50°, 4 angles = 130°. This uses properties that parallel lines create congruent angle relationships."},
                {"problem": "A triangle has angles in ratio 2:3:4. Find the measure of each angle. Then explain why these angles must sum to 180° and why no triangle can have angles 2:3:5.", "answer": "2x + 3x + 4x = 180; 9x = 180; x = 20. Angles: 40°, 60°, 80°. For 2:3:5: 2x + 3x + 5x = 10x = 180; x = 18. Angles: 36°, 54°, 90°. Actually this works! (Hypothetically, 2:3:5 gives 36-54-90 triangle). The sum must be 180° by Triangle Angle Sum Theorem."},
                {"problem": "A transversal crosses two lines. If the two lines are NOT parallel, what can you conclude about the angles formed? Give an example with specific angle measures. How does this differ from the parallel case?", "answer": "Non-parallel lines: corresponding angles are NOT equal, alternate interior angles are NOT equal. Example: transversal crosses one line at 60° and another at 75° (not equal). When lines are parallel, these angles ARE equal. The angle relationships break down unless lines are parallel. This is how we prove lines are parallel—by checking if alternate interior angles equal."}
            ]
        }
    },
    "probability": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "A spinner has 4 equal sections: red, blue, green, yellow. What is the probability of spinning red?", "answer": "1/4 or 0.25 or 25%"},
                {"problem": "A bag has 3 red balls and 7 blue balls. What is the probability of drawing a red ball?", "answer": "3/10 or 0.3 or 30%"},
                {"problem": "A standard die has 6 faces. What is the probability of rolling a 4?", "answer": "1/6 or ≈0.167 or ≈16.7%"}
            ],
            "developing": [
                {"problem": "A bag has 5 red, 3 blue, and 2 green marbles. What is the probability of drawing a non-red marble?", "answer": "P(non-red) = (3+2)/10 = 5/10 = 1/2"},
                {"problem": "Two fair coins are flipped. List all possible outcomes and find the probability of getting exactly one heads.", "answer": "Outcomes: HH, HT, TH, TT. P(one heads) = 2/4 = 1/2"},
                {"problem": "A deck has 52 cards. What is the probability of drawing a heart?", "answer": "13/52 = 1/4 or 0.25"}
            ],
            "proficient": [
                {"problem": "A jar has red and blue marbles. After drawing 1 marble without replacement, what changes about the probability for the next draw? Explain.", "answer": "The total number of marbles decreases by 1, changing the denominator. The probability of each color changes based on what was drawn. P changes because both sample space size and favorable outcomes may change."},
                {"problem": "A spinner has sections: 1/4 red, 1/4 blue, 1/2 green. You spin twice. What is the probability of getting red both times?", "answer": "P(red, red) = 1/4 × 1/4 = 1/16"},
                {"problem": "A bag has 4 red and 6 blue marbles. You draw 2 without replacement. What is P(both same color)?", "answer": "P(both red) = (4/10) × (3/9) = 12/90. P(both blue) = (6/10) × (5/9) = 30/90. P(same) = 12/90 + 30/90 = 42/90 = 7/15"}
            ],
            "extending": [
                {"problem": "A lottery ticket has probability 1/1000 of winning. You buy 10 tickets. What is the probability of winning at least once? Explain your strategy (hint: it's easier to find probability of NOT winning any).", "answer": "P(not win on one) = 999/1000. P(not win on any of 10) = (999/1000)^10 ≈ 0.9900. P(win at least once) = 1 - 0.9900 ≈ 0.0100 or 1%. Using complement rule is simpler than calculating 'at least once' directly."},
                {"problem": "In a class, 15 students play soccer and 10 play basketball. 5 play both. If you randomly pick a student, what is the probability they play at least one sport? Draw a Venn diagram and show your calculation.", "answer": "Total playing = 15 + 10 - 5 = 20. P(sport) = 20/30 = 2/3. (Venn diagram shows overlap of 5, soccer-only of 10, basketball-only of 5)"},
                {"problem": "Compare theoretical probability (expected) vs. experimental probability (observed). Design an experiment: flip a coin 100 times. What do you expect? If you observe 60 heads, explain why this differs from theoretical prediction. What would happen if you flipped 10,000 times?", "answer": "Theoretical: 50 heads (0.5 probability). Experiment gives 60 heads (0.6 observed). Difference due to random variation—small sample. Law of Large Numbers: with 10,000 flips, observed probability converges toward 0.5. Large samples give results closer to theoretical."}
            ]
        }
    },
    "random sampling": {
        "grade": 7,
        "levels": {
            "entry": [
                {"problem": "A school has 500 students. You want to survey 50 randomly selected students about lunch preferences. Is this a random sample?", "answer": "Yes, if selection is random (each student has equal chance)"},
                {"problem": "Explain the difference between surveying 'students at football practice' vs. 'randomly selected students' about favorite sport.", "answer": "Football practice: biased (skews toward football fans). Random selection: unbiased (represents all students equally)"},
                {"problem": "A poll calls people with listed phone numbers. Is this a random sample of all voters?", "answer": "No; it's biased toward people with listed numbers (excludes cell-only users and others)"}
            ],
            "developing": [
                {"problem": "A company wants to know customer satisfaction. Should they survey customers at the store, or send random surveys to their mailing list? Explain the bias in each method.", "answer": "Store survey: biased toward satisfied customers (unsatisfied ones left). Mailing list: could be biased if list is outdated or incomplete. Random phone calls or random selection from database is better."},
                {"problem": "A website offers a survey. Is this a random sample of the population?", "answer": "No; it's a convenience/volunteer sample. Biased toward people who use that website and choose to respond (likely skewed toward engaged users)."},
                {"problem": "To estimate fish population in a lake, researchers mark 50 fish and release them. Later, they catch 100 fish, finding 8 marked ones. Estimate total population.", "answer": "Using proportion: 50/N = 8/100; N = 625 fish (capture-recapture method)"}
            ],
            "proficient": [
                {"problem": "A school wants to know students' views on homework. Compare: (A) survey randomly selected students, (B) survey students' parents, (C) survey teachers. Which gives best info about student views? Why?", "answer": "(A) is best—directly surveys the population of interest. (B) and (C) are indirect/secondhand. Sampling must match the population you're studying. Parents/teachers have different perspectives than students themselves."},
                {"problem": "A survey has 1000 responses showing 60% support for a policy. The margin of error is ±3%. What does this mean? What is the confidence interval?", "answer": "Margin of error of ±3% means if they repeated the survey, 95% of the time the true value would be between 57% and 63%. Confidence interval: 57% to 63%."},
                {"problem": "Explain why a sample of 1000 gives more reliable results than a sample of 100, even if both are random. What's the relationship between sample size and margin of error?", "answer": "Larger samples give more reliable estimates (smaller margin of error). Margin of error decreases as √n increases (if you quadruple sample size, margin of error cuts in half roughly). Bigger samples reduce random variation."}
            ],
            "extending": [
                {"problem": "You want to estimate the proportion of defective items in a factory production run. Design a sampling plan: (a) explain what 'random' means, (b) justify your sample size, (c) describe how bias could occur, (d) how you'd report results with confidence intervals.", "answer": "(a) Random = each item has equal chance. (b) Larger sample reduces margin of error; typical rule is n≥30. (c) Bias if: sample from one shift only, selecting visible items, excluding fast-moving defects. (d) If 5/100 defective: 5% ± 4% (roughly), so 1-9% likely range. State confidence level (95%)."},
                {"problem": "Two polls on an election: Poll A surveyed 500 random voters, poll B surveyed 1000. Poll A shows 52% for candidate X, Poll B shows 48%. Which is more reliable? Can we conclude they're contradictory? Explain with confidence intervals.", "answer": "Poll B is more reliable (larger sample, smaller margin of error). Poll A: 52% ± ~4.5%. Poll B: 48% ± ~3.1%. Their confidence intervals overlap (roughly 47.5-52.5% for B, 47.5-56.5% for A), so they're NOT necessarily contradictory. Polls can show similar true values even with different point estimates."},
                {"problem": "Explain the difference between stratified sampling and simple random sampling. When would stratified be better? Give an example where you're surveying student opinions about school.", "answer": "Simple random: each student equally likely. Stratified: divide into groups (grade 6, 7, 8) and randomly sample from each. Stratified better when subgroups have different views. Example: younger/older students might differ on homework policy; stratified ensures each grade represented proportionally. Captures variation between groups."}
            ]
        }
    },
    "exponents and scientific notation": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "Calculate: 2³", "answer": "8"},
                {"problem": "Write 0.00045 in scientific notation.", "answer": "4.5 × 10⁻⁴"},
                {"problem": "Write 3.2 × 10⁵ in standard form.", "answer": "320,000"}
            ],
            "developing": [
                {"problem": "Calculate: 2² × 2³", "answer": "32 (or 2⁵)"},
                {"problem": "Write 0.000067 in scientific notation.", "answer": "6.7 × 10⁻⁵"},
                {"problem": "Calculate: (10²)³", "answer": "10⁶ = 1,000,000"}
            ],
            "proficient": [
                {"problem": "Simplify: (3²)³ × 3⁻² / 3⁴. Express answer as a power of 3.", "answer": "3⁶ × 3⁻² / 3⁴ = 3⁴ / 3⁴ = 3⁰ = 1"},
                {"problem": "The mass of an electron is about 9.11 × 10⁻³¹ kg. The mass of a proton is about 1.67 × 10⁻²⁷ kg. Which is heavier and by how much? (Divide to find ratio)", "answer": "Proton is heavier. Ratio: (1.67 × 10⁻²⁷) / (9.11 × 10⁻³¹) ≈ 1836 (proton is about 1836 times heavier)"},
                {"problem": "Calculate: 2⁻³ + 2⁻¹", "answer": "1/8 + 1/2 = 1/8 + 4/8 = 5/8"}
            ],
            "extending": [
                {"problem": "A bacteria population doubles every hour. Starting with 100 bacteria, write an exponential expression for the population after h hours. How many bacteria after 8 hours? If you started with different initial amounts, how would the formula change?", "answer": "P(h) = 100 × 2^h. After 8 hours: 100 × 2⁸ = 100 × 256 = 25,600 bacteria. Different initial: P(h) = P₀ × 2^h (changes the coefficient). Base 2 stays same (doubling rate)."},
                {"problem": "A star's luminosity is 2 × 10²⁸ watts. Earth receives luminosity 1.4 × 10³ watts per square meter. Calculate how much total power Earth receives from the star (given Earth's distance and solar constant). Explain the role of exponents in handling huge numbers.", "answer": "Power = luminosity / (4πd²). Exponents let us handle enormous numbers compactly. Without scientific notation, 10²⁸ is hard to write/comprehend. Exponents show scale (order of magnitude): 10²⁸ is vastly larger than 10³."},
                {"problem": "Explain why a^m × a^n = a^(m+n) using the definition of exponents. Then explain why this breaks down for 2^(-3) and how negative exponents redefine things. Verify your answer with 2^2 × 2^(-3).", "answer": "a^m = a×a×...×a (m times); a^n = a×...×a (n times). Product = a^(m+n) (combine all factors). Negative exponents: 2^(-3) = 1/2³ (reciprocal). 2² × 2^(-3) = 2^(2-3) = 2^(-1) = 1/2. Check: 4 × 1/8 = 1/2 ✓. Exponent laws extend consistently to negative exponents."}
            ]
        }
    },
    "square roots and irrational numbers": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "Calculate: √16", "answer": "4"},
                {"problem": "Estimate √10 to the nearest tenth.", "answer": "3.2 (between √9=3 and √16=4)"},
                {"problem": "Is √2 rational or irrational?", "answer": "Irrational (cannot be written as fraction of integers)"}
            ],
            "developing": [
                {"problem": "Calculate: √64 + √36", "answer": "8 + 6 = 14"},
                {"problem": "Simplify: √50", "answer": "5√2 (since √50 = √(25×2) = 5√2)"},
                {"problem": "Estimate π to the nearest hundredth.", "answer": "3.14"}
            ],
            "proficient": [
                {"problem": "Simplify: 3√12 - √27", "answer": "3√12 - √27 = 3(2√3) - 3√3 = 6√3 - 3√3 = 3√3"},
                {"problem": "A square has area 50 cm². Find the side length in simplest radical form.", "answer": "s = √50 = 5√2 cm"},
                {"problem": "Is 7/3 rational or irrational? Explain.", "answer": "Rational; it's a ratio of integers. Can be expressed as a fraction and a terminating or repeating decimal."}
            ],
            "extending": [
                {"problem": "Prove that √2 is irrational using proof by contradiction. (Hint: assume √2 = p/q where p and q have no common factors, then show this leads to a contradiction.)", "answer": "Assume √2 = p/q (lowest terms). Then 2 = p²/q², so p² = 2q². This means p² is even, so p is even. Write p = 2k. Then (2k)² = 2q²; 4k² = 2q²; 2k² = q². So q² is even, making q even. But if p and q both even, they share factor 2, contradicting our assumption. Therefore √2 is irrational."},
                {"problem": "Calculate √18 + √50 - √8 in simplest form. Show each step.", "answer": "√18 = 3√2. √50 = 5√2. √8 = 2√2. Sum: 3√2 + 5√2 - 2√2 = 6√2. Like terms combine when radicals match."},
                {"problem": "Explain why √a + √b ≠ √(a+b) using a counterexample. Under what conditions can you simplify radical expressions? Why is √(ab) = √a × √b true?", "answer": "Counter: √4 + √4 = 2 + 2 = 4, but √(4+4) = √8 ≈ 2.83. Addition doesn't work inside radicals. √(ab) = √a × √b because both equal √(a×b) when we expand factors. You can simplify radicals when factors are perfect squares (pull out integers) or combine like radicals (same radicand)."}
            ]
        }
    },
    "linear functions": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "Is y = 2x + 3 a linear function? Plot three points.", "answer": "Yes. Points: (0,3), (1,5), (2,7) form a straight line."},
                {"problem": "Find the slope of the line through (0,0) and (2,4).", "answer": "Slope = (4-0)/(2-0) = 2"},
                {"problem": "A line has equation y = -1x + 5. What is the y-intercept?", "answer": "5 (when x=0, y=5)"}
            ],
            "developing": [
                {"problem": "Write the equation of a line with slope 3 and y-intercept -2.", "answer": "y = 3x - 2"},
                {"problem": "Find the slope of the line through (1,2) and (4,8).", "answer": "Slope = (8-2)/(4-1) = 6/3 = 2"},
                {"problem": "Graph the line y = -2x + 4. Identify slope and y-intercept.", "answer": "Slope: -2. Y-intercept: 4. Line goes down 2 for every right 1 unit."}
            ],
            "proficient": [
                {"problem": "Find the equation of a line passing through (1,3) and (4,9). Write in slope-intercept form.", "answer": "Slope = (9-3)/(4-1) = 2. Using point-slope: y - 3 = 2(x - 1); y = 2x + 1"},
                {"problem": "Two lines: y = 2x + 3 and y = -1/2 x + 5. Are they perpendicular? Explain.", "answer": "Yes; slopes are 2 and -1/2, and 2 × (-1/2) = -1. Perpendicular lines have slopes whose product is -1."},
                {"problem": "A phone plan costs $30/month plus $0.05 per text message. Write a linear equation for total cost C as a function of texts t.", "answer": "C = 0.05t + 30"}
            ],
            "extending": [
                {"problem": "A company's profit grows linearly over time. In year 1, profit was $50,000. In year 5, profit was $130,000. Find the equation P(t) where t is years. When will profit reach $250,000?", "answer": "Slope = (130,000-50,000)/(5-1) = 20,000. P(t) = 20,000t + 30,000. At $250,000: 250,000 = 20,000t + 30,000; 220,000 = 20,000t; t = 11 years."},
                {"problem": "Three points lie on a line: (1,4), (3,10), and (x,16). Find x. Explain why any two points determine the line, and a third point must satisfy the equation.", "answer": "Slope from first two: (10-4)/(3-1) = 3. Line: y = 3x + 1. For third point: 16 = 3x + 1; 3x = 15; x = 5. Any two points determine slope and intercept uniquely. Third point must satisfy the equation or the three are not collinear."},
                {"problem": "Compare: A line with slope 1/2 and a line with slope 2. Which is steeper? Explain the relationship between slope values and visual steepness. What does slope 0 represent?", "answer": "Slope 2 is steeper (rises 2 units per 1 unit right vs. 1 per 2). Larger |slope| = steeper. Slope 0 = horizontal line (no change in y). Negative slope = decreasing line. Slope magnitude indicates rate of change visually."}
            ]
        }
    },
    "systems of equations": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "Solve by substitution: y = 2x and x + y = 6", "answer": "Substitute: x + 2x = 6; 3x = 6; x = 2, y = 4"},
                {"problem": "Solve by graphing: y = x + 1 and y = -x + 3. Where do they intersect?", "answer": "Intersection at (1, 2)"},
                {"problem": "Do these lines intersect? y = 2x + 1 and y = 2x + 3. Explain.", "answer": "No; they're parallel (same slope, different y-intercepts). No solution."}
            ],
            "developing": [
                {"problem": "Solve by elimination: 2x + y = 7 and x - y = 2", "answer": "Add equations: 3x = 9; x = 3. Substitute: 3 - y = 2; y = 1. Solution: (3, 1)"},
                {"problem": "Solve: 3x + 2y = 12 and x + y = 5", "answer": "From second: x = 5 - y. Substitute: 3(5-y) + 2y = 12; 15 - 3y + 2y = 12; -y = -3; y = 3, x = 2"},
                {"problem": "How many solutions do these lines have? y = 3x + 2 and 2y = 6x + 4", "answer": "Infinitely many (the lines are the same—one is a multiple of the other)"}
            ],
            "proficient": [
                {"problem": "Solve: 2x + 3y = 13 and 4x - y = 5. Show each step.", "answer": "From second: y = 4x - 5. Substitute: 2x + 3(4x-5) = 13; 2x + 12x - 15 = 13; 14x = 28; x = 2. y = 4(2) - 5 = 3. Solution: (2,3)"},
                {"problem": "Solve by elimination: 3x + 4y = 10 and 2x - 4y = 0", "answer": "Add: 5x = 10; x = 2. From second: 2(2) - 4y = 0; 4 = 4y; y = 1. Solution: (2, 1)"},
                {"problem": "A coffee shop sells coffee ($3) and tea ($2). Total sales: $120. Let c = coffees, t = teas. Write a system if they sold 50 drinks total.", "answer": "3c + 2t = 120 and c + t = 50. Solving: from second, t = 50-c. Substitute: 3c + 2(50-c) = 120; 3c + 100 - 2c = 120; c = 20 (coffees), t = 30 (teas)."}
            ],
            "extending": [
                {"problem": "A system has equations 2x - y = 4 and 4x - 2y = 8. How many solutions? Explain why. Then modify one equation to create a system with exactly one solution.", "answer": "Infinitely many (second is 2× first; same line). Change to: 2x - y = 4 and 4x - 2y = 10 (now inconsistent, no solution) or 2x - y = 4 and x + y = 2 (one solution: (2,0)). Different slopes = one solution, parallel = no solution, same line = infinite."},
                {"problem": "A farm grows corn and wheat. Corn needs 2 workers per acre, wheat needs 3. They have 50 total workers. Corn generates $200/acre profit, wheat $250/acre. They have 20 acres total. Write and solve a system to maximize profit. What constraints limit this optimization?", "answer": "Let c = corn acres, w = wheat acres. Constraints: c + w = 20 and 2c + 3w = 50. Solving: from first, c = 20-w. Substitute: 2(20-w) + 3w = 50; 40 - 2w + 3w = 50; w = 10, c = 10. Profit = 200(10) + 250(10) = $4500. Constraints: land availability (20 acres) and labor (50 workers)."},
                {"problem": "Explain what it means geometrically when a system has no solution, one solution, or infinite solutions. How do you determine this algebraically before solving?", "answer": "No solution: parallel lines (same slope, different intercepts). One solution: intersecting lines (different slopes). Infinite: same line (one equation multiple of other). Algebraically: compare slopes and intercepts, or solve and check if you get contradiction (no solution), unique values (one solution), or identity like 0=0 (infinite)."}
            ]
        }
    },
    "multi-step equations": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "Solve: 2(x + 3) = 14", "answer": "2x + 6 = 14; 2x = 8; x = 4"},
                {"problem": "Solve: 3x - 5 = 16", "answer": "3x = 21; x = 7"},
                {"problem": "Solve: x/3 + 2 = 5", "answer": "x/3 = 3; x = 9"}
            ],
            "developing": [
                {"problem": "Solve: 4(x - 2) + 3 = 11", "answer": "4x - 8 + 3 = 11; 4x - 5 = 11; 4x = 16; x = 4"},
                {"problem": "Solve: 2x + 5 = x + 10", "answer": "2x - x = 10 - 5; x = 5"},
                {"problem": "Solve: 3(2x - 1) = 2x + 9", "answer": "6x - 3 = 2x + 9; 4x = 12; x = 3"}
            ],
            "proficient": [
                {"problem": "Solve: 2(x + 3) - 5 = 3(x - 1). Check your solution.", "answer": "2x + 6 - 5 = 3x - 3; 2x + 1 = 3x - 3; 1 + 3 = 3x - 2x; x = 4. Check: 2(7) - 5 = 14 - 5 = 9; 3(3) = 9 ✓"},
                {"problem": "Solve: -2(x + 4) + 3x = 8 - (x - 2)", "answer": "-2x - 8 + 3x = 8 - x + 2; x - 8 = 10 - x; 2x = 18; x = 9"},
                {"problem": "A rectangle has length 5 cm more than width. Perimeter is 50 cm. Write and solve an equation to find dimensions.", "answer": "Let w = width. Perimeter: 2(w + (w+5)) = 50; 2(2w+5) = 50; 4w + 10 = 50; 4w = 40; w = 10 cm, length = 15 cm"}
            ],
            "extending": [
                {"problem": "Solve: 3(2x + 1) - 2(x - 3) = 5(x - 2) + 1. Show each step and verify your answer.", "answer": "6x + 3 - 2x + 6 = 5x - 10 + 1; 4x + 9 = 5x - 9; 9 + 9 = 5x - 4x; x = 18. Verify: 3(37) - 2(15) = 111 - 30 = 81; 5(16) + 1 = 81 ✓"},
                {"problem": "Solve for x: a(x + b) = c + dx. Justify each step. Explain why the solution depends on the values of a and d.", "answer": "ax + ab = c + dx; ax - dx = c - ab; x(a - d) = c - ab; x = (c - ab)/(a - d). Solution requires a ≠ d (if a = d, equation has no/infinite solutions). Shows how parameters affect solvability."},
                {"problem": "A student made an error solving 3(x + 2) = 15. They got 3x + 2 = 15, then x = 13/3. Identify the error, show correct solution, and explain why the distributive property is essential here.", "answer": "Error: forgot to distribute 3 to the 2. Should be 3x + 6 = 15; 3x = 9; x = 3. Distributive property requires multiplying both terms inside parentheses. Without it, the equation changes and solution is wrong. Error check: 3(3+2) = 15 → 3(5) = 15 ✓; 3(13/3 + 2) ≠ 15."}
            ]
        }
    },
    "pythagorean theorem": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "A right triangle has legs 3 and 4. Find the hypotenuse.", "answer": "c² = 3² + 4² = 9 + 16 = 25; c = 5"},
                {"problem": "A right triangle has hypotenuse 10 and one leg 6. Find the other leg.", "answer": "6² + b² = 10²; 36 + b² = 100; b² = 64; b = 8"},
                {"problem": "Is a triangle with sides 5, 12, 13 a right triangle?", "answer": "Yes; 5² + 12² = 25 + 144 = 169 = 13²"}
            ],
            "developing": [
                {"problem": "A ladder leans against a wall. The ladder is 13 feet long and the base is 5 feet from the wall. How high does it reach?", "answer": "5² + h² = 13²; 25 + h² = 169; h² = 144; h = 12 feet"},
                {"problem": "Find the diagonal of a rectangle with length 8 m and width 6 m.", "answer": "d² = 8² + 6² = 64 + 36 = 100; d = 10 m"},
                {"problem": "A right triangle has legs √2 and 1. Find the hypotenuse.", "answer": "c² = (√2)² + 1² = 2 + 1 = 3; c = √3"}
            ],
            "proficient": [
                {"problem": "A ship travels 7 miles east, then 5 miles north. How far is it from the starting point?", "answer": "Distance² = 7² + 5² = 49 + 25 = 74; Distance = √74 ≈ 8.6 miles"},
                {"problem": "A right triangle has hypotenuse 15 cm. The two legs are in ratio 3:4. Find each leg.", "answer": "Let legs be 3k and 4k. (3k)² + (4k)² = 15²; 9k² + 16k² = 225; 25k² = 225; k = 3. Legs: 9 cm and 12 cm."},
                {"problem": "A square has side length 5. Find the diagonal using the Pythagorean theorem.", "answer": "d² = 5² + 5² = 50; d = √50 = 5√2 ≈ 7.07"}
            ],
            "extending": [
                {"problem": "Prove that (3,4,5), (5,12,13), and (8,15,17) are Pythagorean triples. Find a pattern to generate more triples. Use the formula: for integers m > n > 0, the triple is (m²-n², 2mn, m²+n²).", "answer": "Verify: 3² + 4² = 5² ✓; 5² + 12² = 13² ✓; 8² + 15² = 17² ✓. Using formula with m=2, n=1: (3,4,5). m=3, n=2: (5,12,13). m=4, n=1: (15,8,17). Formula generates all primitive triples."},
                {"problem": "In a right triangle, if you know the hypotenuse and one leg, explain why you can always find the other leg (assuming real solutions). What happens if the given leg is longer than the hypotenuse?", "answer": "Use c² = a² + b²; b² = c² - a². Always solvable if c > a (hypotenuse must be longest side). If a > c, then b² < 0 (no real solution), violating triangle inequality. The Pythagorean theorem depends on right triangle structure: hypotenuse is always the longest side."},
                {"problem": "A 3D problem: A rectangular box has dimensions 3×4×5. Find the diagonal from one corner to the opposite corner. (Hint: use Pythagorean theorem twice.)", "answer": "First diagonal of base: d₁² = 3² + 4² = 25; d₁ = 5. Space diagonal: d² = 5² + 5² = 50; d = √50 = 5√2 ≈ 7.07. Or directly: d² = 3² + 4² + 5² = 50 (3D Pythagorean formula)."}
            ]
        }
    },
    "transformations": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "A point (2,3) is reflected across the x-axis. What are the new coordinates?", "answer": "(2,-3)"},
                {"problem": "A point (1,2) is translated 3 units right and 2 units up. New coordinates?", "answer": "(4,4)"},
                {"problem": "A figure is rotated 90° clockwise around the origin. The point (2,0) moves to which point?", "answer": "(0,-2)"}
            ],
            "developing": [
                {"problem": "Reflect (3,4) across the y-axis.", "answer": "(-3,4)"},
                {"problem": "Rotate (3,0) counterclockwise 90° around origin.", "answer": "(0,3)"},
                {"problem": "Translate triangle ABC with vertices (1,1), (3,1), (2,3) by 2 right and 1 down. New vertices?", "answer": "(3,0), (5,0), (4,2)"}
            ],
            "proficient": [
                {"problem": "A figure has vertices (0,0), (2,0), (2,2), (0,2). It's rotated 180° around the origin. List the new vertices.", "answer": "(0,0), (-2,0), (-2,-2), (0,-2)"},
                {"problem": "Reflect the triangle with vertices (1,2), (4,1), (3,4) across the line y=x.", "answer": "(2,1), (1,4), (4,3) (swap x and y coordinates)"},
                {"problem": "A point (4,3) is reflected across y-axis, then translated 5 units down. Final position?", "answer": "After reflection: (-4,3). After translation: (-4,-2)"}
            ],
            "extending": [
                {"problem": "A shape undergoes two transformations: rotation 90° counterclockwise around origin, then reflection across x-axis. Find the final location of point (2,3). Explain why the order matters.", "answer": "After rotation: (2,3) → (-3,2). After reflection: (-3,-2). If reversed: reflection (-2,3) → rotation (3,2). Order matters; transformations are not always commutative. Composition of transformations depends on sequence."},
                {"problem": "Design a sequence of transformations that moves the point (1,0) to the point (-1,-1). Show at least two different ways to do this.", "answer": "Method 1: Rotate 90° CCW: (0,1). Translate left 1, down 2: (-1,-1). Method 2: Translate left 2, down 1: (-1,-1). Method 3: Reflect across y-axis: (-1,0). Translate down 1: (-1,-1). Multiple solutions show transformations can be combined flexibly."},
                {"problem": "Explain why a reflection followed by another reflection across parallel lines is equivalent to a translation. Use an example with lines y=0 and y=1.", "answer": "Reflect (0,0) across y=0: (0,0). Reflect across y=1: (0,2). Net result: translation 2 units up. This is a composition: two reflections across parallel lines equal a translation perpendicular to both lines, with distance = 2× distance between lines. Shows deep connection between transformations."}
            ]
        }
    },
    "congruence and similarity": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "Are these triangles congruent? Triangle A: sides 3,4,5. Triangle B: sides 3,4,5.", "answer": "Yes (SSS: same three sides)"},
                {"problem": "Are these triangles similar? Triangle A: angles 30°,60°,90°. Triangle B: angles 30°,60°,90°.", "answer": "Yes (AAA: same angles)"},
                {"problem": "A shape is scaled by factor 2. Is the original and scaled shape congruent or similar?", "answer": "Similar (same angles, proportional sides), not congruent (different sizes)"}
            ],
            "developing": [
                {"problem": "Triangle ABC has sides 6,8,10. Triangle DEF has sides 3,4,5. Are they similar? How do you know?", "answer": "Yes; all ratios 6:3 = 8:4 = 10:5 = 2:1. Proportional sides means similar."},
                {"problem": "If two triangles are congruent, are they similar?", "answer": "Yes; congruence is a special case of similarity (scale factor 1:1)"},
                {"problem": "Triangle PQR has angles 40°, 60°, 80°. Triangle XYZ has angles 40°, 60°, 80°. Are they congruent? Similar?", "answer": "Similar (same angles). Congruent only if sides also match (need side lengths)."}
            ],
            "proficient": [
                {"problem": "Two rectangles: Rectangle A is 4×6. Rectangle B is 6×9. Are they similar? If so, find the scale factor.", "answer": "Yes; 4:6 = 6:9? 24 ≠ 36. Actually, 4/6 ≠ 6/9. Let me recalc: 4/6 = 2/3 and 6/9 = 2/3. Yes, similar with scale factor 2:3."},
                {"problem": "Two triangles are similar with scale factor 2:3. If the smaller has area 20 cm², what's the area of the larger?", "answer": "Area scales by (scale factor)². (3/2)² = 9/4. Larger area = 20 × 9/4 = 45 cm²"},
                {"problem": "Prove two triangles congruent using SAS (Side-Angle-Side). Triangle ABC: AB=5, angle B=60°, BC=7. Triangle DEF: DE=5, angle E=60°, EF=7. Are they congruent?", "answer": "Yes, by SAS. Two sides and included angle match exactly."}
            ],
            "extending": [
                {"problem": "A map uses scale 1:1000. Two cities appear 5 cm apart on map. On a second map with scale 1:500, how far apart do they appear? Explain why changing scale affects representation but not real distance.", "answer": "First map: real distance = 5 × 1000 = 5000 cm. Second map: distance = 5000 / 500 = 10 cm. Real distance is fixed; map representation changes with scale. Smaller scale ratio (1:500) means larger representation."},
                {"problem": "If a 3D object is scaled by factor k, how do volume and surface area change? Explain using a cube with side s.", "answer": "Original cube: SA = 6s², V = s³. Scaled by k: SA' = 6(ks)² = 6k²s² (multiplied by k²). V' = (ks)³ = k³s³ (multiplied by k³). Surface area scales by k²; volume scales by k³. This explains why small organisms have high surface-area-to-volume ratios."},
                {"problem": "Two triangles are similar. The sides of the first are 5, 12, 13. Two sides of the second are 10 and 24. Find the third side of the second triangle. Explain how similarity guarantees unique solutions.", "answer": "Scale factor: 10/5 = 2. Third side: 13 × 2 = 26. Similarity ensures all corresponding sides scale by same factor, making solution unique and determinate (no ambiguity)."}
            ]
        }
    },
    "volume of cylinders cones spheres": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "Find volume of a cylinder with radius 2 cm and height 5 cm. Use π ≈ 3.14", "answer": "V = πr²h ≈ 3.14 × 4 × 5 ≈ 62.8 cm³"},
                {"problem": "A cone has radius 3 m and height 4 m. Find its volume.", "answer": "V = (1/3)πr²h ≈ (1/3) × 3.14 × 9 × 4 ≈ 37.68 m³"},
                {"problem": "A sphere has radius 5 inches. Find its volume.", "answer": "V = (4/3)πr³ ≈ (4/3) × 3.14 × 125 ≈ 523.33 in³"}
            ],
            "developing": [
                {"problem": "A cylinder has volume 100 cm³ and radius 2 cm. Find height.", "answer": "V = πr²h; 100 = 3.14 × 4 × h; h ≈ 7.96 cm"},
                {"problem": "Compare volumes: cylinder (r=2, h=6) vs. cone (r=2, h=6).", "answer": "Cylinder ≈ 75.4 units³. Cone ≈ 25.1 units³. Cylinder is 3× cone (V_cone = (1/3)V_cylinder)"},
                {"problem": "A sphere has diameter 10 cm. Find volume.", "answer": "Radius = 5 cm. V = (4/3)πr³ ≈ 523.33 cm³"}
            ],
            "proficient": [
                {"problem": "A water tank shaped like a cylinder has radius 2 m and height 3 m. How many liters does it hold? (1 m³ = 1000 L)", "answer": "V = πr²h ≈ 3.14 × 4 × 3 ≈ 37.68 m³ ≈ 37,680 L"},
                {"problem": "An ice cream cone has radius 2 cm and height 8 cm. A scoop (hemisphere) has radius 2 cm. Find total volume.", "answer": "Cone: (1/3)π(4)(8) ≈ 33.5 cm³. Hemisphere: (2/3)π(8) ≈ 16.75 cm³. Total ≈ 50.3 cm³"},
                {"problem": "Two spheres: sphere A has radius 2 cm, sphere B has radius 4 cm. Compare volumes.", "answer": "Sphere A: V ≈ 33.5 cm³. Sphere B: V ≈ 268 cm³. Ratio: 268/33.5 = 8 = 2³ (radius doubled, volume × 8)"}
            ],
            "extending": [
                {"problem": "A cylindrical pipe has inner radius 1 cm and outer radius 1.5 cm, with length 50 cm. Find volume of material (hollow region removed). Explain step-by-step.", "answer": "Outer volume: π(1.5)²(50) ≈ 353.25 cm³. Inner volume: π(1)²(50) ≈ 157 cm³. Material volume ≈ 196.25 cm³. This is finding volume of an annular (ring-shaped) cylinder."},
                {"problem": "A cone and sphere have same radius r. If cone's volume equals sphere's, what is relationship between heights? (V_cone = (1/3)πr²h, V_sphere = (4/3)πr³)", "answer": "(1/3)πr²h = (4/3)πr³; h = 4r. Cone must be 4 times as tall as its radius to equal sphere volume. Shows how different shapes can enclose same volume."},
                {"problem": "A company makes chocolate truffles (spheres, radius 1 cm). A box holds them in a 3×4 grid stacked 2 high. What's the volume of chocolate? (V = (4/3)π). How much air space in a box that fits them? Assume box is exactly sized.", "answer": "One truffle: V ≈ 4.19 cm³. Total: 3×4×2×4.19 ≈ 100.48 cm³. Box dimensions: 6 cm × 8 cm × 4 cm = 192 cm³. Air space ≈ 91.52 cm³. Shows packaging efficiency."}
            ]
        }
    },
    "scatter plots": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "Create a scatter plot for: (1,2), (2,4), (3,6), (4,8). Describe the relationship.", "answer": "Points form straight line (positive correlation). As x increases, y increases proportionally (y=2x)."},
                {"problem": "Do these points show positive, negative, or no correlation? (1,5), (2,4), (3,3), (4,2)", "answer": "Negative correlation (as x increases, y decreases)"},
                {"problem": "Plot points (1,1), (2,3), (3,2), (4,4), (5,3). Describe relationship.", "answer": "Weak positive relationship; data scattered but general upward trend"}
            ],
            "developing": [
                {"problem": "A scatter plot shows study time (hours) vs. test score. Points roughly follow line y = 10x + 60. If you study 3 hours, what score do you predict?", "answer": "y = 10(3) + 60 = 90 points"},
                {"problem": "Data: Student hours studied: 1,2,3,4,5. Test scores: 60,70,75,85,95. Plot these and draw a line of best fit.", "answer": "Points show strong positive correlation. Line roughly y = 7x + 53 (or similar). Slope ≈ 7 (each hour adds ~7 points)."},
                {"problem": "A scatter plot has r = 0.95. How strong is the relationship?", "answer": "Very strong positive correlation (r close to +1)"}
            ],
            "proficient": [
                {"problem": "Data for a car: age (years) vs. value ($1000s). (0,25), (1,22), (2,20), (3,18), (4,15). Find line of best fit and predict value at 6 years.", "answer": "Negative correlation. Line roughly y = -2.5x + 25. At 6 years: y ≈ 10 ($10,000). Depreciation rate ≈ $2500/year."},
                {"problem": "Two scatter plots: Plot A has r = 0.3, Plot B has r = 0.8. Which shows stronger relationship? What does r measure?", "answer": "Plot B (r = 0.8 closer to ±1). r measures strength and direction of linear relationship (-1 to +1). r = 0 means no linear relationship."},
                {"problem": "Create a scatter plot and line of best fit for: Temperature (°F): 50, 60, 70, 80, 90. Ice cream sales: 100, 150, 200, 280, 350. Find predicted sales at 75°F.", "answer": "Strong positive correlation. Line roughly y = 5x - 150. At 75°F: y ≈ 225 units sold."}
            ],
            "extending": [
                {"problem": "A scatter plot shows hours worked vs. hourly pay with r = 0.02. Interpret this. What might explain such a weak correlation? How is this different from causation?", "answer": "r ≈ 0 means no linear relationship. Possible: many factors affect pay (skill, role, experience, not hours worked). Correlation ≠ causation: even if related, doesn't mean one causes the other. Hours worked may not directly determine pay."},
                {"problem": "Data on height (inches) vs. test score for 100 students shows r = -0.08. A student claims 'taller students do worse on tests.' Critique this using correlation concepts.", "answer": "Incorrect. r = -0.08 shows almost no relationship (not meaningful). Even if negative, weak correlation doesn't support strong claims. Would need r < -0.5 for noteworthy relationship, plus consideration of confounding variables (height doesn't cause test performance)."},
                {"problem": "Explain why extrapolation beyond the data range is risky in scatter plots. Give an example of a relationship that's linear in one range but not in another.", "answer": "Extrapolation assumes pattern continues (may not). Example: plant growth is roughly linear early (y ≈ 2x) but plateaus (levels off) at maturity—not linear forever. Predicting beyond observed range risks large errors. Use caution and domain knowledge when extending trends."}
            ]
        }
    },
    "two-way frequency tables": {
        "grade": 8,
        "levels": {
            "entry": [
                {"problem": "A table shows favorite sports: Soccer: 15 boys, 10 girls. Basketball: 12 boys, 18 girls. Total surveyed?", "answer": "15+10+12+18 = 55"},
                {"problem": "From above, what fraction of soccer players are girls?", "answer": "10/(15+10) = 10/25 = 2/5"},
                {"problem": "Create a two-way frequency table with categories: Has phone (yes/no) and Age (under 13, 13+). Example: under 13 with phone: 5. Under 13 no phone: 20. 13+ with phone: 45. 13+ no phone: 10.", "answer": "Table: Rows: under 13 (5, 20, 25), 13+ (45, 10, 55). Columns: Has phone, No phone, Total. Grand total: 80."}
            ],
            "developing": [
                {"problem": "A two-way table: Favorite color. Blue: 30 males, 35 females. Red: 20 males, 25 females. Total females who prefer blue?", "answer": "35/(35+25) = 35/60 = 7/12 of females prefer blue"},
                {"problem": "From a survey: Plays sports (yes/no) and Grade (6, 7, 8). Grade 6: 20 yes, 30 no. Grade 7: 25 yes, 25 no. Grade 8: 18 yes, 32 no. Create table and find percentage of grade 6 students surveyed.", "answer": "Total: 20+30+25+25+18+32=150. Grade 6: 50. Percentage: 50/150 ≈ 33.3%"},
                {"problem": "Do more grade 7 or grade 8 students play sports? (Use data above)", "answer": "Grade 7: 25. Grade 8: 18. More grade 7 students play sports."}
            ],
            "proficient": [
                {"problem": "A two-way frequency table shows: Prefers cats vs. dogs, by Gender. Females: 40 cats, 30 dogs (70 total). Males: 20 cats, 50 dogs (70 total). Total 140. Find P(prefers cats) and P(female | prefers cats).", "answer": "P(prefers cats) = 60/140 = 3/7. P(female | prefers cats) = 40/60 = 2/3."},
                {"problem": "A survey: Likes math (yes/no) and Has calculator (yes/no). Create a table with 200 total: 60 like math with calc, 40 like math without, 50 don't like math with calc, 50 don't like with. Find P(has calculator).", "answer": "Has calc: 60+50=110. P(has calc) = 110/200 = 11/20 = 0.55"},
                {"problem": "From the frequency table, find P(likes math | has calculator). Is liking math independent of having a calculator?", "answer": "P(likes math | has calc) = 60/110 = 6/11 ≈ 0.545. P(likes math overall) = 100/200 = 0.5. Not exactly equal, so not independent (though close)."}
            ],
            "extending": [
                {"problem": "A medical test for disease has 95% accuracy. If 2% of population has disease, create a two-way frequency table (assume 10,000 people) showing: Test positive/negative vs. Has disease/no disease. Find P(disease | positive test).", "answer": "Has disease: 200. True positive: 190. False negative: 10. No disease: 9800. False positive: 490. True negative: 9310. P(disease | positive) = 190/(190+490) ≈ 0.279. Despite high accuracy, most positive tests are false (explains why positive doesn't mean you have disease)."},
                {"problem": "A school tracks: College-bound vs. Not, and whether student took SAT prep. Design a table that would help the school decide if SAT prep affects college outcomes. What data would convince you of causation vs. correlation?", "answer": "Table: 4 cells (college-bound/not × SAT prep/no prep). High proportion of college-bound in prep group suggests effect, but correlation. For causation: need controlled experiment (random assignment to prep vs. control) or adjust for confounding (prior grades, motivation)."},
                {"problem": "Explain how a two-way frequency table can reveal Simpson's Paradox: a trend appearing in subgroups but reversing in combined data. Give an example with hypothetical hiring data.", "answer": "Example: Department A hired 3/4 women (75%), 2/4 men (50%). Department B: 2/3 women (67%), 4/5 men (80%). Both departments hired higher % of women. But combined: 5/7 women (71%) vs. 6/9 men (67%)—appears to favor women overall, but each department favors men! Occurs when subgroup sizes differ drastically. Shows importance of examining data at multiple levels."}
            ]
        }
    }
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_teaching_insights_by_grade(grade):
    """Return all teaching insights for a specific grade level."""
    return {topic: data for topic, data in TEACHING_INSIGHTS_COMPLETE.items() 
            if data.get('grade') == grade}


def get_risa_dialogues_by_grade(grade):
    """Return all RISA dialogues for a specific grade level."""
    return {topic: data for topic, data in RISA_DIALOGUES_COMPLETE.items() 
            if data.get('grade') == grade}


def get_leveled_problems_by_grade(grade):
    """Return all leveled problems for a specific grade level."""
    return {topic: data for topic, data in LEVELED_PROBLEMS_COMPLETE.items() 
            if data.get('grade') == grade}


def get_all_topics_by_grade(grade):
    """Return all available topics for a grade level."""
    topics = set()
    for db in [TEACHING_INSIGHTS_COMPLETE, RISA_DIALOGUES_COMPLETE, LEVELED_PROBLEMS_COMPLETE]:
        for topic, data in db.items():
            if data.get('grade') == grade:
                topics.add(topic)
    return sorted(topics)


def search_topic(query):
    """Search for a topic across all databases using fuzzy matching.
    
    Args:
        query: search string (e.g., 'pythagorean', 'linear', 'fractions')
    
    Returns:
        dict with keys 'teaching_insights', 'risa_dialogues', 'leveled_problems'
        containing matched data from each database.
    """
    query_lower = query.lower().strip()
    result = {
        'teaching_insights': None,
        'risa_dialogues': None, 
        'leveled_problems': None,
        'topic': None,
        'grade': None
    }
    
    # Try exact match first
    for db_name, db in [('teaching_insights', TEACHING_INSIGHTS_COMPLETE), 
                         ('risa_dialogues', RISA_DIALOGUES_COMPLETE),
                         ('leveled_problems', LEVELED_PROBLEMS_COMPLETE)]:
        if query_lower in db:
            result[db_name] = db[query_lower]
            result['topic'] = query_lower
            result['grade'] = db[query_lower].get('grade')
    
    # If no exact match, try partial match
    if result['topic'] is None:
        for db_name, db in [('teaching_insights', TEACHING_INSIGHTS_COMPLETE),
                             ('risa_dialogues', RISA_DIALOGUES_COMPLETE),
                             ('leveled_problems', LEVELED_PROBLEMS_COMPLETE)]:
            for topic_key in db:
                if query_lower in topic_key or topic_key in query_lower:
                    result[db_name] = db[topic_key]
                    if result['topic'] is None:
                        result['topic'] = topic_key
                        result['grade'] = db[topic_key].get('grade')
                    break
        
        # Fill in any remaining None databases using the matched topic
        if result['topic']:
            for db_name, db in [('teaching_insights', TEACHING_INSIGHTS_COMPLETE),
                                 ('risa_dialogues', RISA_DIALOGUES_COMPLETE),
                                 ('leveled_problems', LEVELED_PROBLEMS_COMPLETE)]:
                if result[db_name] is None and result['topic'] in db:
                    result[db_name] = db[result['topic']]
    
    return result
