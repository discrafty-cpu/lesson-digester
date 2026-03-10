#!/usr/bin/env python3
"""
THE LESSON DIGESTER — MCA-III Standards Alignment Module
Minnesota Comprehensive Assessments — Series III
Mathematics Test Specifications for Grades 7, 8

This module provides:
1. Complete benchmark database with descriptions, vocabulary, and cognitive complexity
2. Topic-to-standard mapping for CPM lesson alignment
3. Vocabulary extraction for embedding in slide discussions
4. Gap analysis to flag missing standards coverage
5. Standards-based quiz/assessment item generator
6. AI image prompt generator for lesson visuals
"""

# ─── COGNITIVE COMPLEXITY LEVELS ──────────────────────────────
COMPLEXITY = {
    "A": "Recall — demonstrate knowledge of facts, terms, properties, or procedures",
    "B": "Skill/Concept — use information or conceptual knowledge; two or more steps",
    "C": "Strategic Thinking — use reasoning, planning, evidence, or higher-order thinking",
}

# ─── GRADE 7 STANDARDS ──────────────────────────────────────────
GRADE_7 = {
    # ── Strand 1: Number & Operation (12-16 items) ──
    "7.1.1.1": {
        "description": "Know that every rational number can be written as the ratio of two integers or as a terminating or repeating decimal. Recognize that π is not rational, approximated by 22/7 and 3.14.",
        "vocabulary": ["terminating", "repeating", "rational", "irrational", "π"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Number & Operation",
    },
    "7.1.1.2": {
        "description": "Understand that division of two integers always results in a rational number. Interpret decimal results of division using a calculator.",
        "vocabulary": ["terminating", "repeating"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Number & Operation",
    },
    "7.1.1.3": {
        "description": "Locate positive and negative rational numbers on a number line, understand opposites, and plot pairs on a coordinate grid.",
        "vocabulary": ["opposite", "coordinate", "origin"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Number & Operation",
    },
    "7.1.1.4": {
        "description": "Compare positive and negative rational numbers expressed in various forms using <, >, =, ≤, ≥.",
        "vocabulary": [],
        "complexity": "A",
        "items": "4-6",
        "strand": "Number & Operation",
    },
    "7.1.1.5": {
        "description": "Recognize and generate equivalent representations of positive and negative rational numbers, including equivalent fractions.",
        "vocabulary": ["equivalent"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Number & Operation",
    },
    "7.1.2.1": {
        "description": "Add, subtract, multiply and divide positive and negative rational numbers (integers, fractions, terminating decimals); use efficient procedures; raise positive rational numbers to whole-number exponents.",
        "vocabulary": ["exponent"],
        "complexity": "A",
        "items": "8-10",
        "strand": "Number & Operation",
    },
    "7.1.2.2": {
        "description": "Use real-world contexts and inverse relationships between addition and subtraction to explain arithmetic with negative rational numbers.",
        "vocabulary": ["inverse"],
        "complexity": "B",
        "items": "8-10",
        "strand": "Number & Operation",
    },
    "7.1.2.3": {
        "description": "Understand that calculators and other computing technologies often truncate or round numbers.",
        "vocabulary": ["truncate", "round"],
        "complexity": "A",
        "items": "8-10",
        "strand": "Number & Operation",
        "note": "Assessed within 7.1.2.4",
    },
    "7.1.2.4": {
        "description": "Solve problems involving calculations with positive and negative rational numbers and positive integer exponents, including simple and compound interest.",
        "vocabulary": ["simple interest", "compound interest"],
        "complexity": "B",
        "items": "8-10",
        "strand": "Number & Operation",
    },
    "7.1.2.5": {
        "description": "Use proportional reasoning to solve problems involving ratios in various contexts.",
        "vocabulary": ["proportion", "ratio"],
        "complexity": "B",
        "items": "8-10",
        "strand": "Number & Operation",
    },
    "7.1.2.6": {
        "description": "Demonstrate understanding of the relationship between absolute value and distance on a number line. Use the symbol for absolute value.",
        "vocabulary": ["absolute value"],
        "complexity": "B",
        "items": "8-10",
        "strand": "Number & Operation",
    },

    # ── Strand 2: Algebra (13-18 items) ──
    "7.2.1.1": {
        "description": "Understand that a relationship between x and y is proportional if it can be expressed as y/x = k or y = kx. Distinguish from other relationships including inversely proportional (xy = k).",
        "vocabulary": ["proportional", "inversely", "constant of proportionality"],
        "complexity": "B",
        "items": "1-2",
        "strand": "Algebra",
    },
    "7.2.1.2": {
        "description": "Understand that the graph of a proportional relationship is a line through the origin whose slope is the unit rate (constant of proportionality). Use graphing technology to examine changes.",
        "vocabulary": ["proportional", "origin", "slope", "unit rate"],
        "complexity": "B",
        "items": "1-2",
        "strand": "Algebra",
    },
    "7.2.2.1": {
        "description": "Represent proportional relationships with tables, verbal descriptions, symbols, equations and graphs; translate between representations. Determine the unit rate (constant of proportionality or slope).",
        "vocabulary": ["proportional", "origin", "slope", "constant of proportionality"],
        "complexity": "B",
        "items": "5-7",
        "strand": "Algebra",
    },
    "7.2.2.2": {
        "description": "Solve multi-step problems involving proportional relationships (discounts, tax, percent of change).",
        "vocabulary": ["proportional", "discount", "tax", "percent of change"],
        "complexity": "C",
        "items": "5-7",
        "strand": "Algebra",
    },
    "7.2.2.3": {
        "description": "Use knowledge of proportions to assess the reasonableness of solutions.",
        "vocabulary": ["proportion", "reasonable"],
        "complexity": "B",
        "items": "5-7",
        "strand": "Algebra",
        "note": "Assessed within 7.2.2.1 and 7.2.2.2",
    },
    "7.2.2.4": {
        "description": "Represent real-world or mathematical situations using equations and inequalities involving variables and positive and negative rational numbers.",
        "vocabulary": ["equation", "inequality", "variable"],
        "complexity": "B",
        "items": "5-7",
        "strand": "Algebra",
    },
    "7.2.3.1": {
        "description": "Use properties of algebra to generate equivalent numerical and algebraic expressions (associative, commutative, distributive laws); grouping symbols and whole number exponents.",
        "vocabulary": ["simplify", "associative", "commutative", "distributive"],
        "complexity": "A",
        "items": "3-4",
        "strand": "Algebra",
    },
    "7.2.3.2": {
        "description": "Evaluate algebraic expressions containing rational numbers and whole number exponents at specified values (max 3 variables).",
        "vocabulary": ["evaluate", "substitute"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Algebra",
    },
    "7.2.3.3": {
        "description": "Apply understanding of order of operations and grouping symbols when using calculators.",
        "vocabulary": ["order of operations"],
        "complexity": "A",
        "items": "3-4",
        "strand": "Algebra",
        "note": "Assessed within 7.2.3.1 and 7.2.3.2",
    },
    "7.2.4.1": {
        "description": "Represent relationships in various contexts with equations involving variables and positive and negative rational numbers. Use properties of equality to solve. Interpret in context.",
        "vocabulary": ["equation", "variable", "properties of equality"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Algebra",
    },
    "7.2.4.2": {
        "description": "Solve equations resulting from proportional relationships in various contexts.",
        "vocabulary": ["proportion"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Algebra",
    },

    # ── Strand 3: Geometry & Measurement (7-9 items) ──
    "7.3.1.1": {
        "description": "Demonstrate understanding of the proportional relationship between diameter and circumference. The constant of proportionality is π. Calculate circumference and area of circles.",
        "vocabulary": ["radius", "diameter", "circumference", "π", "area", "sector", "arc length"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Geometry & Measurement",
    },
    "7.3.1.2": {
        "description": "Calculate the volume and surface area of cylinders and justify the formulas used.",
        "vocabulary": ["radius", "diameter", "circumference", "cylinder", "lateral area", "volume", "surface area"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Geometry & Measurement",
    },
    "7.3.2.1": {
        "description": "Describe properties of similarity, compare geometric figures for similarity and determine scale factors.",
        "vocabulary": ["similar", "corresponding", "scale factor", "congruent"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Geometry & Measurement",
    },
    "7.3.2.2": {
        "description": "Apply scale factors, length ratios and area ratios to determine side lengths and areas of similar geometric figures.",
        "vocabulary": ["similar", "corresponding", "scale factor"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Geometry & Measurement",
    },
    "7.3.2.3": {
        "description": "Use proportions and ratios to solve problems involving scale drawings and conversions of measurement units.",
        "vocabulary": ["similar", "corresponding", "scale drawing", "conversion"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Geometry & Measurement",
    },
    "7.3.2.4": {
        "description": "Graph and describe translations and reflections of figures on a coordinate grid, and determine coordinates after transformation.",
        "vocabulary": ["translation", "reflection", "transformation", "coordinate"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Geometry & Measurement",
    },

    # ── Strand 4: Data Analysis & Probability (7-9 items) ──
    "7.4.1.1": {
        "description": "Design simple experiments and collect data. Determine mean, median and range. Use these to draw conclusions, compare data sets and make predictions.",
        "vocabulary": ["mean", "median", "range", "stem-and-leaf plot"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Data Analysis & Probability",
    },
    "7.4.1.2": {
        "description": "Describe the impact of inserting or deleting a data point on the mean and median. Create data displays using spreadsheets.",
        "vocabulary": ["outlier"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Data Analysis & Probability",
    },
    "7.4.2.1": {
        "description": "Use reasoning with proportions to display and interpret data in circle graphs (pie charts) and histograms. Choose appropriate data display.",
        "vocabulary": ["circle graph", "histogram", "frequency table"],
        "complexity": "B",
        "items": "1-2",
        "strand": "Data Analysis & Probability",
    },
    "7.4.3.1": {
        "description": "Use random numbers to simulate situations involving randomness, make a histogram, and compare results to known probabilities.",
        "vocabulary": ["random", "simulation", "histogram"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Data Analysis & Probability",
        "note": "Not assessed on MCA-III",
    },
    "7.4.3.2": {
        "description": "Calculate probability as a fraction of sample space or area. Express probabilities as percents, decimals and fractions.",
        "vocabulary": ["probability", "sample space"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Data Analysis & Probability",
    },
    "7.4.3.3": {
        "description": "Use proportional reasoning to draw conclusions about and predict relative frequencies of outcomes based on probabilities.",
        "vocabulary": ["relative frequency", "probability"],
        "complexity": "C",
        "items": "3-4",
        "strand": "Data Analysis & Probability",
    },
}

# ─── GRADE 8 STANDARDS ──────────────────────────────────────────
GRADE_8 = {
    # ── Strand 1: Number & Operation (6-8 items) ──
    "8.1.1.1": {
        "description": "Classify real numbers as rational or irrational. Know that √ of a non-perfect-square is irrational. Sum/product rules for rational/irrational.",
        "vocabulary": ["irrational", "real", "square root", "radical"],
        "complexity": "B",
        "items": "6-8",
        "strand": "Number & Operation",
    },
    "8.1.1.2": {
        "description": "Compare real numbers; locate on a number line. Identify √ of a positive integer as integer or between two consecutive integers.",
        "vocabulary": ["square root", "radical", "consecutive"],
        "complexity": "B",
        "items": "6-8",
        "strand": "Number & Operation",
    },
    "8.1.1.3": {
        "description": "Determine rational approximations for solutions involving real numbers.",
        "vocabulary": ["square root", "radical", "consecutive", "approximation"],
        "complexity": "B",
        "items": "6-8",
        "strand": "Number & Operation",
    },
    "8.1.1.4": {
        "description": "Know and apply properties of positive and negative integer exponents to generate equivalent numerical expressions.",
        "vocabulary": ["exponent", "base", "power"],
        "complexity": "B",
        "items": "6-8",
        "strand": "Number & Operation",
    },
    "8.1.1.5": {
        "description": "Express approximations using scientific notation; multiply and divide numbers in scientific notation; use correct significant digits.",
        "vocabulary": ["scientific notation", "significant digits", "standard form"],
        "complexity": "B",
        "items": "6-8",
        "strand": "Number & Operation",
    },

    # ── Strand 2: Algebra (18-29 items) ──
    "8.2.1.1": {
        "description": "Understand that a function is a relationship between independent and dependent variables. Use functional notation f(x).",
        "vocabulary": ["independent", "dependent", "constant", "coefficient", "function"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Algebra",
    },
    "8.2.1.2": {
        "description": "Use linear functions to represent relationships where change in input leads to constant-times-that change in output.",
        "vocabulary": ["independent", "dependent", "constant", "coefficient", "linear"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Algebra",
    },
    "8.2.1.3": {
        "description": "Understand that a function is linear if f(x) = mx + b or its graph is a straight line.",
        "vocabulary": ["linear", "constant", "coefficient"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Algebra",
    },
    "8.2.1.4": {
        "description": "Understand that an arithmetic sequence is a linear function f(x) = mx + b, where x = 0,1,2,3,...",
        "vocabulary": ["nth term", "arithmetic sequence", "geometric sequence", "linear function", "non-linear function", "common difference", "progression"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Algebra",
    },
    "8.2.1.5": {
        "description": "Understand that a geometric sequence is a non-linear function f(x) = ab^x, where x = 0,1,2,3,...",
        "vocabulary": ["nth term", "arithmetic sequence", "geometric sequence", "linear function", "non-linear function", "exponential", "common ratio", "progression"],
        "complexity": "B",
        "items": "4-5",
        "strand": "Algebra",
    },
    "8.2.2.1": {
        "description": "Represent linear functions with tables, verbal descriptions, symbols, equations and graphs; translate between representations.",
        "vocabulary": ["linear function"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Algebra",
    },
    "8.2.2.2": {
        "description": "Identify graphical properties of linear functions including slopes and intercepts. Slope = rate of change; y-intercept = 0 when proportional.",
        "vocabulary": ["linear function", "intercept", "slope", "rate of change"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Algebra",
    },
    "8.2.2.3": {
        "description": "Identify how coefficient changes in f(x) = mx + b affect graphs of linear functions. Use graphing technology.",
        "vocabulary": ["linear function", "intercept", "coefficient", "constant"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Algebra",
    },
    "8.2.2.4": {
        "description": "Represent arithmetic sequences using equations, tables, graphs and verbal descriptions; solve problems.",
        "vocabulary": ["nth term", "arithmetic sequence", "geometric sequence", "linear function", "non-linear function", "progression"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Algebra",
    },
    "8.2.2.5": {
        "description": "Represent geometric sequences using equations, tables, graphs and verbal descriptions; solve problems.",
        "vocabulary": ["nth term", "arithmetic sequence", "geometric sequence", "linear function", "non-linear function", "progression"],
        "complexity": "B",
        "items": "4-6",
        "strand": "Algebra",
    },
    "8.2.3.1": {
        "description": "Evaluate algebraic expressions including radicals and absolute values at specified values.",
        "vocabulary": ["simplify", "evaluate"],
        "complexity": "A",
        "items": "2-4",
        "strand": "Algebra",
    },
    "8.2.3.2": {
        "description": "Justify steps in generating equivalent expressions by identifying properties (associative, commutative, distributive, order of operations).",
        "vocabulary": ["associative", "commutative", "distributive", "identity", "property", "order of operations"],
        "complexity": "B",
        "items": "2-4",
        "strand": "Algebra",
    },
    "8.2.4.1": {
        "description": "Use linear equations to represent situations involving constant rate of change, including proportional and non-proportional.",
        "vocabulary": ["rate of change", "proportional", "linear"],
        "complexity": "B",
        "items": "8-14",
        "strand": "Algebra",
    },
    "8.2.4.2": {
        "description": "Solve multi-step equations in one variable. Solve for one variable in a multi-variable equation. Justify steps by identifying properties of equalities.",
        "vocabulary": ["multi-step", "properties of equality"],
        "complexity": "B",
        "items": "8-14",
        "strand": "Algebra",
    },
    "8.2.4.3": {
        "description": "Express linear equations in slope-intercept, point-slope and standard forms; convert between them. Find an equation of a line.",
        "vocabulary": ["slope-intercept form", "point-slope form", "standard form"],
        "complexity": "B",
        "items": "8-14",
        "strand": "Algebra",
    },
    "8.2.4.4": {
        "description": "Use linear inequalities to represent relationships in various contexts (max 1 variable).",
        "vocabulary": ["inequality"],
        "complexity": "B",
        "items": "8-14",
        "strand": "Algebra",
    },
    "8.2.4.5": {
        "description": "Solve linear inequalities using properties of inequalities. Graph solutions on a number line.",
        "vocabulary": ["inequality", "solution set"],
        "complexity": "B",
        "items": "8-14",
        "strand": "Algebra",
    },
    "8.2.4.6": {
        "description": "Represent relationships with equations and inequalities involving absolute value of a linear expression. Solve and graph solutions.",
        "vocabulary": ["absolute value"],
        "complexity": "B",
        "items": "8-14",
        "strand": "Algebra",
    },
    "8.2.4.7": {
        "description": "Represent relationships using systems of linear equations. Solve symbolically, graphically and numerically.",
        "vocabulary": ["system of equations", "undefined", "infinite", "intersecting", "identical"],
        "complexity": "C",
        "items": "8-14",
        "strand": "Algebra",
    },
    "8.2.4.8": {
        "description": "Understand that a system of linear equations may have 0, 1, or infinite solutions. Relate to intersecting/parallel/identical lines. Check solutions by substitution.",
        "vocabulary": ["system of equations", "parallel", "intersecting"],
        "complexity": "B",
        "items": "8-14",
        "strand": "Algebra",
        "note": "Assessed within 8.2.4.7",
    },
    "8.2.4.9": {
        "description": "Use the relationship between square roots and squares of a number to solve problems.",
        "vocabulary": ["square root"],
        "complexity": "B",
        "items": "8-14",
        "strand": "Algebra",
    },

    # ── Strand 3: Geometry & Measurement (6-8 items) ──
    "8.3.1.1": {
        "description": "Use the Pythagorean Theorem to solve problems involving right triangles.",
        "vocabulary": ["Pythagorean Theorem", "hypotenuse", "right triangle"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Geometry & Measurement",
    },
    "8.3.1.2": {
        "description": "Determine distance between two points on horizontal/vertical lines and use Pythagorean Theorem for any two points in a coordinate system.",
        "vocabulary": ["Pythagorean Theorem", "distance"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Geometry & Measurement",
    },
    "8.3.1.3": {
        "description": "Informally justify the Pythagorean Theorem using measurements, diagrams and computer software.",
        "vocabulary": ["Pythagorean Theorem"],
        "complexity": "C",
        "items": "3-4",
        "strand": "Geometry & Measurement",
        "note": "Not assessed on MCA-III",
    },
    "8.3.2.1": {
        "description": "Understand and apply relationships between slopes of parallel lines and perpendicular lines.",
        "vocabulary": ["parallel", "perpendicular", "slope"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Geometry & Measurement",
    },
    "8.3.2.2": {
        "description": "Analyze polygons on a coordinate system by determining the slopes of their sides.",
        "vocabulary": ["polygon", "slope"],
        "complexity": "B",
        "items": "3-4",
        "strand": "Geometry & Measurement",
    },
    "8.3.2.3": {
        "description": "Given a line on a coordinate system and a point not on the line, find lines through that point that are parallel and perpendicular to the given line.",
        "vocabulary": ["parallel", "perpendicular"],
        "complexity": "C",
        "items": "3-4",
        "strand": "Geometry & Measurement",
    },

    # ── Strand 4: Data Analysis & Probability (6-7 items) ──
    "8.4.1.1": {
        "description": "Collect, display and interpret data using scatterplots. Estimate a line of best fit and determine an equation for it.",
        "vocabulary": ["scatterplot", "line of best fit", "correlation"],
        "complexity": "B",
        "items": "6-7",
        "strand": "Data Analysis & Probability",
    },
    "8.4.1.2": {
        "description": "Use a line of best fit to approximate rate of change and make predictions about values not in the original data set.",
        "vocabulary": ["scatterplot", "line of best fit", "rate of change"],
        "complexity": "B",
        "items": "6-7",
        "strand": "Data Analysis & Probability",
    },
    "8.4.1.3": {
        "description": "Assess the reasonableness of predictions using scatterplots by interpreting in the original context.",
        "vocabulary": ["scatterplot", "line of best fit", "prediction"],
        "complexity": "C",
        "items": "6-7",
        "strand": "Data Analysis & Probability",
    },
}

# ─── TOPIC → STANDARD MAPPING ──────────────────────────────────
# Maps CPM lesson topics / keywords to relevant MCA-III benchmarks
TOPIC_MAP = {
    # --- Grade 7 Topics ---
    "distance rate time": ["7.2.1.1", "7.2.1.2", "7.2.2.1", "7.2.2.2", "7.2.4.1"],
    "proportional relationships": ["7.2.1.1", "7.2.1.2", "7.2.2.1", "7.2.2.2", "7.2.2.3"],
    "scaling": ["7.3.2.1", "7.3.2.2", "7.3.2.3"],
    "scale factor": ["7.3.2.1", "7.3.2.2", "7.3.2.3"],
    "scale drawing": ["7.3.2.3"],
    "circumference": ["7.3.1.1"],
    "area of circle": ["7.3.1.1"],
    "pi": ["7.1.1.1", "7.3.1.1"],
    "diameter": ["7.3.1.1"],
    "radius": ["7.3.1.1"],
    "cylinder": ["7.3.1.2"],
    "volume": ["7.3.1.2"],
    "surface area": ["7.3.1.2"],
    "percent": ["7.2.2.2"],
    "discount": ["7.2.2.2"],
    "tax": ["7.2.2.2"],
    "percent of change": ["7.2.2.2"],
    "proportion": ["7.1.2.5", "7.2.2.1", "7.2.2.2", "7.2.4.2"],
    "ratio": ["7.1.2.5", "7.2.2.1"],
    "unit rate": ["7.2.1.1", "7.2.1.2"],
    "constant of proportionality": ["7.2.1.1", "7.2.1.2", "7.2.2.1"],
    "slope": ["7.2.1.2"],
    "integer operations": ["7.1.2.1", "7.1.2.2"],
    "negative numbers": ["7.1.1.3", "7.1.1.4", "7.1.2.1", "7.1.2.2"],
    "absolute value": ["7.1.2.6"],
    "exponents": ["7.1.2.1", "7.1.2.4"],
    "interest": ["7.1.2.4"],
    "simple interest": ["7.1.2.4"],
    "compound interest": ["7.1.2.4"],
    "equivalent expressions": ["7.2.3.1", "7.2.3.2"],
    "distributive property": ["7.2.3.1"],
    "order of operations": ["7.2.3.3"],
    "equations": ["7.2.4.1", "7.2.4.2"],
    "inequalities": ["7.2.2.4"],
    "similarity": ["7.3.2.1", "7.3.2.2"],
    "transformations": ["7.3.2.4"],
    "translations": ["7.3.2.4"],
    "reflections": ["7.3.2.4"],
    "mean median range": ["7.4.1.1", "7.4.1.2"],
    "data analysis": ["7.4.1.1", "7.4.1.2", "7.4.2.1"],
    "histogram": ["7.4.2.1"],
    "circle graph": ["7.4.2.1"],
    "probability": ["7.4.3.2", "7.4.3.3"],
    "multiplier": ["7.3.1.1", "7.2.1.1", "7.2.2.1"],  # 9.1.1 "What is the Multiplier"

    # --- Grade 8 Topics ---
    "linear functions": ["8.2.1.1", "8.2.1.2", "8.2.1.3", "8.2.2.1", "8.2.2.2"],
    "slope intercept": ["8.2.4.3", "8.2.2.2"],
    "systems of equations": ["8.2.4.7", "8.2.4.8"],
    "pythagorean theorem": ["8.3.1.1", "8.3.1.2"],
    "irrational numbers": ["8.1.1.1", "8.1.1.2"],
    "scientific notation": ["8.1.1.5"],
    "arithmetic sequence": ["8.2.1.4", "8.2.2.4"],
    "geometric sequence": ["8.2.1.5", "8.2.2.5"],
    "scatterplot": ["8.4.1.1", "8.4.1.2", "8.4.1.3"],
    "line of best fit": ["8.4.1.1", "8.4.1.2"],
    "parallel perpendicular": ["8.3.2.1", "8.3.2.2", "8.3.2.3"],
    "rate of change": ["8.2.4.1", "8.2.2.2"],
    "function notation": ["8.2.1.1"],
    "linear inequalities": ["8.2.4.4", "8.2.4.5"],
    "square roots": ["8.1.1.1", "8.1.1.2", "8.2.4.9"],
}


# ─── ALIGNMENT FUNCTIONS ─────────────────────────────────────────

def get_standards_db(grade=None):
    """Return the full standards database, optionally filtered by grade."""
    if grade == 7:
        return GRADE_7
    elif grade == 8:
        return GRADE_8
    else:
        combined = {}
        combined.update(GRADE_7)
        combined.update(GRADE_8)
        return combined


def align_lesson(topic_keywords, grade=None):
    """
    Given a list of topic keywords from a lesson, return aligned MCA-III benchmarks.

    Args:
        topic_keywords: list of strings like ["circumference", "pi", "diameter"]
        grade: optional int (7 or 8) to filter

    Returns:
        dict with:
            - benchmarks: list of (benchmark_id, description, complexity) tuples
            - vocabulary: deduplicated list of all required vocabulary
            - strands_covered: set of strand names
            - gaps: list of strands NOT covered (for warning)
    """
    db = get_standards_db(grade)
    matched_ids = set()

    for kw in topic_keywords:
        kw_lower = kw.lower().strip()
        # Direct topic map lookup
        if kw_lower in TOPIC_MAP:
            for bid in TOPIC_MAP[kw_lower]:
                if bid in db:
                    matched_ids.add(bid)
        # Fuzzy: check if keyword appears in any benchmark description
        for bid, spec in db.items():
            if kw_lower in spec["description"].lower():
                matched_ids.add(bid)

    # Build results
    benchmarks = []
    all_vocab = set()
    strands = set()

    for bid in sorted(matched_ids):
        spec = db[bid]
        benchmarks.append({
            "id": bid,
            "description": spec["description"],
            "complexity": spec["complexity"],
            "strand": spec["strand"],
            "vocabulary": spec["vocabulary"],
        })
        all_vocab.update(spec["vocabulary"])
        strands.add(spec["strand"])

    # Gap analysis
    all_strands = set(spec["strand"] for spec in db.values())
    gaps = all_strands - strands

    return {
        "benchmarks": benchmarks,
        "vocabulary": sorted(all_vocab),
        "strands_covered": sorted(strands),
        "gaps": sorted(gaps),
    }


def get_vocabulary_for_lesson(topic_keywords, grade=None):
    """Extract just the vocabulary list for a lesson's topics."""
    result = align_lesson(topic_keywords, grade)
    return result["vocabulary"]


def format_standards_report(topic_keywords, lesson_name="", grade=None):
    """
    Generate a human-readable standards alignment report.

    Returns a formatted string suitable for printing or embedding.
    """
    result = align_lesson(topic_keywords, grade)

    lines = []
    lines.append(f"═══ MCA-III STANDARDS ALIGNMENT ═══")
    if lesson_name:
        lines.append(f"Lesson: {lesson_name}")
    lines.append(f"Topics: {', '.join(topic_keywords)}")
    lines.append(f"Grade: {grade or '7-8'}")
    lines.append("")

    # Benchmarks by strand
    by_strand = {}
    for b in result["benchmarks"]:
        by_strand.setdefault(b["strand"], []).append(b)

    for strand in sorted(by_strand.keys()):
        lines.append(f"── {strand} ──")
        for b in by_strand[strand]:
            complexity_label = {"A": "Recall", "B": "Skill/Concept", "C": "Strategic Thinking"}[b["complexity"]]
            lines.append(f"  {b['id']} [{b['complexity']}: {complexity_label}]")
            lines.append(f"    {b['description'][:120]}...")
            if b["vocabulary"]:
                lines.append(f"    Vocab: {', '.join(b['vocabulary'])}")
        lines.append("")

    # Vocabulary summary
    lines.append(f"── KEY VOCABULARY ({len(result['vocabulary'])} terms) ──")
    lines.append(f"  {', '.join(result['vocabulary'])}")
    lines.append("")

    # Gap analysis
    if result["gaps"]:
        lines.append(f"⚠  STRANDS NOT COVERED: {', '.join(result['gaps'])}")
        lines.append(f"   Consider adding problems or discussion that address these areas.")
    else:
        lines.append(f"✓  All strands covered!")

    return "\n".join(lines)


def generate_vocab_discussion_prompts(vocabulary_list):
    """
    Generate role-specific discussion prompts that emphasize vocabulary.

    Returns a list of (role, prompt) tuples ready for embedding in slides.
    """
    if not vocabulary_list:
        return []

    # Pick up to 4 key terms
    terms = vocabulary_list[:4]

    prompts = [
        ("Facilitator",
         f'Read the problem aloud. Ask: "Can someone explain what {terms[0]} means in this problem?"'),
        ("Resource Manager",
         f'What tools or information do we need? Make sure everyone can define: {", ".join(terms[:2])}.'),
        ("Task Manager",
         f'Before we start, let\'s make sure we can use the word{"s" if len(terms) > 1 else ""} {", ".join(terms[:3])} in a sentence about this problem.'),
        ("Recorder Reporter",
         f'Write down our answer using the vocabulary: {", ".join(terms[:3])}. Be ready to share.'),
    ]

    return prompts


def generate_vocab_sentence_frames(vocabulary_list, context=""):
    """
    Generate sentence frames that require students to use vocabulary.

    Returns a list of sentence frame strings.
    """
    frames = []
    for term in vocabulary_list[:6]:
        frames.append(f'The {term} in this problem is _____ because _____.')

    if context:
        frames.append(f'In this {context}, we used _____ to find _____.')

    return frames


# ─── STANDARDS QUIZ / TEST GENERATOR ──────────────────────────

# Assessment item templates keyed by benchmark ID.
# Each template has a complexity level and a list of item patterns.
# Patterns use {var} placeholders that get filled with contextual values.

ASSESSMENT_TEMPLATES = {
    # --- Geometry: Circles ---
    "7.3.1.1": [
        {"complexity": "A", "stem": "What is the circumference of a circle with diameter {d} cm?",
         "answer": "C = π × {d} = {c_val} cm", "type": "open"},
        {"complexity": "B", "stem": "A circular fountain has a radius of {r} feet. What is its area? Use π ≈ 3.14.",
         "answer": "A = π × {r}² = {a_val} ft²", "type": "open"},
        {"complexity": "B", "stem": "The circumference of a wheel is {c} inches. What is the diameter?",
         "answer": "d = C ÷ π = {c} ÷ 3.14 ≈ {d_val} inches", "type": "open"},
        {"complexity": "C", "stem": "A circle has area {a} cm². A second circle has double the radius. How many times larger is its area? Explain.",
         "answer": "4 times larger. Doubling r means area = π(2r)² = 4πr².", "type": "extended"},
    ],
    # --- Proportional Relationships ---
    "7.2.1.1": [
        {"complexity": "A", "stem": "Is y = {k}x a proportional relationship? Explain.",
         "answer": "Yes, it can be written as y/x = {k}, a constant ratio.", "type": "open"},
        {"complexity": "B", "stem": "The table shows x: 2, 4, 6 and y: {y1}, {y2}, {y3}. Is this proportional? Find k.",
         "answer": "Yes. k = y/x = {k} for all rows.", "type": "open"},
    ],
    "7.2.2.1": [
        {"complexity": "B", "stem": "A car travels at a constant speed. After {t} hours it has gone {d} miles. Write an equation.",
         "answer": "d = {rate}t, where the unit rate is {rate} mph.", "type": "open"},
        {"complexity": "C", "stem": "Two runners: A goes {d1} miles in {t1} hours, B goes {d2} miles in {t2} hours. Who is faster? Justify with a graph or table.",
         "answer": "Compare unit rates: A = {r1} mph, B = {r2} mph.", "type": "extended"},
    ],
    # --- Number & Operation ---
    "7.1.1.1": [
        {"complexity": "A", "stem": "Is π rational or irrational? Explain.",
         "answer": "Irrational. Its decimal never terminates or repeats.", "type": "open"},
        {"complexity": "B", "stem": "Write 0.{rep} as a fraction.",
         "answer": "Use algebra: let x = 0.{rep}..., then solve.", "type": "open"},
    ],
    # --- Similarity & Scale ---
    "7.3.2.1": [
        {"complexity": "B", "stem": "Two rectangles: 3×5 and 6×10. Are they similar? What is the scale factor?",
         "answer": "Yes. Scale factor = 2.", "type": "open"},
        {"complexity": "C", "stem": "A map uses a scale of 1 inch = {scale} miles. Two cities are {inches} inches apart on the map. What is the real distance?",
         "answer": "{inches} × {scale} = {real} miles.", "type": "open"},
    ],
    # --- Linear Functions (Grade 8) ---
    "8.2.2.2": [
        {"complexity": "B", "stem": "Find the slope and y-intercept of y = {m}x + {b}.",
         "answer": "Slope = {m}, y-intercept = {b}.", "type": "open"},
    ],
    "8.3.1.1": [
        {"complexity": "B", "stem": "A right triangle has legs of {a} and {b}. Find the hypotenuse.",
         "answer": "c = √({a}² + {b}²) = √{sum} ≈ {c_val}", "type": "open"},
    ],
}

import random

def generate_quiz_items(topic_keywords, num_items=5, grade=None, complexity_mix=None):
    """
    Generate assessment items aligned to MCA-III benchmarks for the given topics.

    Args:
        topic_keywords: list of topic strings
        num_items: how many items to generate (default 5)
        grade: 7 or 8 (or None for both)
        complexity_mix: dict like {"A": 1, "B": 3, "C": 1} or None for auto

    Returns:
        list of dicts: [{stem, answer, benchmark, complexity, type}, ...]
    """
    # Get aligned benchmarks
    alignment = align_lesson(topic_keywords, grade=grade)
    matched_ids = [b["id"] for b in alignment["benchmarks"]]

    # Collect available templates
    available = []
    for bid in matched_ids:
        if bid in ASSESSMENT_TEMPLATES:
            for tmpl in ASSESSMENT_TEMPLATES[bid]:
                available.append({"benchmark": bid, **tmpl})

    if not available:
        # Fallback: generate generic items from benchmark descriptions
        for b in alignment["benchmarks"][:num_items]:
            available.append({
                "benchmark": b["id"],
                "complexity": b["complexity"],
                "stem": f"[{b['complexity']}] Demonstrate: {b['description'][:100]}...",
                "answer": "(Student response based on benchmark)",
                "type": "open",
            })

    # Apply complexity mix if specified
    if complexity_mix:
        selected = []
        for level, count in complexity_mix.items():
            pool = [a for a in available if a["complexity"] == level]
            selected.extend(random.sample(pool, min(count, len(pool))))
    else:
        # Default: mix of complexities
        selected = available[:]

    # Shuffle and limit
    random.shuffle(selected)
    items = selected[:num_items]

    # Fill in template variables with reasonable values
    for item in items:
        item["stem"] = _fill_template(item["stem"])
        item["answer"] = _fill_template(item["answer"])

    return items


def _fill_template(text):
    """Fill {var} placeholders with contextual math values."""
    import re
    import math

    # Generate some random but reasonable values
    r = random.choice([3, 4, 5, 6, 7, 8, 10])
    d = 2 * r
    k = random.choice([2, 3, 4, 5, 7])

    replacements = {
        "r": str(r),
        "d": str(d),
        "c_val": f"{round(math.pi * d, 2)}",
        "a_val": f"{round(math.pi * r * r, 2)}",
        "c": str(round(math.pi * d, 1)),
        "d_val": str(round(math.pi * d / math.pi, 1)),
        "a": str(round(math.pi * r * r, 1)),
        "k": str(k),
        "y1": str(k * 2), "y2": str(k * 4), "y3": str(k * 6),
        "t": str(random.choice([2, 3, 4, 5])),
        "rate": str(random.choice([30, 45, 55, 60, 65])),
        "d1": "6", "t1": "2", "d2": "10", "t2": "3",
        "r1": "3", "r2": "3.33",
        "rep": random.choice(["333", "666", "142857"]),
        "scale": str(random.choice([5, 10, 25, 50])),
        "inches": str(random.choice([3, 4, 6, 8])),
        "real": "",  # computed below
        "m": str(random.choice([2, 3, -1, -2, 0.5])),
        "b": str(random.choice([1, -3, 4, 0, -2])),
        "sum": "", "c_val_pyth": "",  # computed below
    }

    # Compute dependent values
    scale = int(replacements["scale"]) if replacements["scale"].isdigit() else 10
    inches = int(replacements["inches"]) if replacements["inches"].isdigit() else 4
    replacements["real"] = str(scale * inches)

    a_leg = random.choice([3, 5, 6, 8])
    b_leg = random.choice([4, 8, 12])
    replacements["a"] = str(a_leg)
    replacements["b"] = str(b_leg)
    replacements["sum"] = str(a_leg**2 + b_leg**2)
    replacements["c_val"] = str(round(math.sqrt(a_leg**2 + b_leg**2), 2))

    for var, val in replacements.items():
        text = text.replace(f"{{{var}}}", val)

    return text


def format_quiz(topic_keywords, num_items=5, lesson_name="", grade=None):
    """
    Generate a formatted quiz ready for a slide or worksheet.

    Returns a dict with:
        - items: list of {stem, answer, benchmark, complexity, type}
        - header: formatted header string
        - standards_covered: list of benchmark IDs
    """
    items = generate_quiz_items(topic_keywords, num_items=num_items, grade=grade)

    header = f"Standards Check: {lesson_name}" if lesson_name else "Standards Check"
    standards = list(set(item["benchmark"] for item in items))

    return {
        "header": header,
        "items": items,
        "standards_covered": sorted(standards),
    }


# ─── LEVELED DIFFERENTIATED PROBLEMS GENERATOR ──────────────

# Proficiency levels aligned to DOK and MCA-III cognitive complexity
PROFICIENCY_LEVELS = {
    "beginning": {
        "label": "Beginning",
        "color_hex": "EF4444",   # red
        "dok": 1,                # Recall
        "complexity": "A",
        "description": "Single-step, direct recall or simple computation",
        "scaffolding": "Friendly numbers, visual supports, sentence starters provided",
        "verb_bank": ["identify", "recall", "calculate", "find", "name", "list", "define"],
    },
    "partial": {
        "label": "Partial Understanding",
        "color_hex": "D4870F",   # amber
        "dok": 2,                # Skill/Concept
        "complexity": "B",
        "description": "Multi-step with some scaffolding, apply a known procedure",
        "scaffolding": "Steps partially guided, some visual support",
        "verb_bank": ["solve", "explain", "compare", "classify", "organize", "estimate"],
    },
    "proficient": {
        "label": "Proficient",
        "color_hex": "3B82F6",   # blue
        "dok": 2,                # Skill/Concept (higher)
        "complexity": "B",
        "description": "Multi-step without scaffolding, apply concepts to new situations",
        "scaffolding": "No scaffolding, grade-level numbers and vocabulary",
        "verb_bank": ["apply", "demonstrate", "construct", "interpret", "justify", "model"],
    },
    "exemplary": {
        "label": "Exemplary",
        "color_hex": "0D9488",   # teal
        "dok": 3,                # Strategic Thinking
        "complexity": "C",
        "description": "Non-routine, requires reasoning, multiple representations, or justification",
        "scaffolding": "Open-ended, requires explanation and mathematical argument",
        "verb_bank": ["analyze", "prove", "evaluate", "create", "design", "critique", "generalize"],
    },
}

# Topic-specific leveled problem templates
# Each topic maps to a dict with 4 levels, each containing 3 problem templates
LEVELED_PROBLEM_BANK = {
    "area of circle": {
        "beginning": [
            {"stem": "A circle has a radius of {r} cm. What is the area? Use A = π × r².", "answer": "A = π × {r}² = {a_val} cm²", "hint": "Multiply the radius by itself, then multiply by π (≈ 3.14)"},
            {"stem": "A circular table has a radius of 3 feet. What is its area? Round to the nearest whole number.", "answer": "A = π × 3² = π × 9 ≈ 28 ft²", "hint": "Area = π × radius × radius"},
            {"stem": "Which formula gives the area of a circle?\n(a) A = 2πr   (b) A = πr²   (c) A = πd", "answer": "(b) A = πr²", "hint": "Area uses radius SQUARED"},
        ],
        "partial": [
            {"stem": "A circular garden has a diameter of {d} meters. Find the area.", "answer": "r = {d} ÷ 2 = {r}, A = π × {r}² = {a_val} m²", "hint": "First find the radius (half the diameter)"},
            {"stem": "A pizza has an area of about 113 square inches. What is the approximate radius?", "answer": "113 = πr², r² = 113 ÷ π ≈ 36, r = 6 inches", "hint": "Work backwards: divide area by π, then take square root"},
            {"stem": "A sprinkler waters a circular area with radius 8 ft. A second sprinkler has radius 4 ft. How many times greater is the first area?", "answer": "π(8²) ÷ π(4²) = 64 ÷ 16 = 4 times greater", "hint": "Calculate both areas, then divide"},
        ],
        "proficient": [
            {"stem": "A circular swimming pool has a circumference of 31.4 meters. Find the area of the pool.", "answer": "C = πd → d = 31.4 ÷ π = 10, r = 5, A = π(5²) = 78.5 m²", "hint": ""},
            {"stem": "Marcus needs to cover a circular table (diameter {d} ft) with fabric that costs $2.50 per square foot. How much will the fabric cost?", "answer": "A = π({r})² = {a_val} ft², Cost = {a_val} × $2.50", "hint": ""},
            {"stem": "A dart board has an outer circle with radius 9 inches and a bullseye with radius 1.5 inches. What percent of the board is the bullseye?", "answer": "Bullseye = π(1.5²) = 7.07, Total = π(9²) = 254.47, Percent = 7.07 ÷ 254.47 ≈ 2.8%", "hint": ""},
        ],
        "exemplary": [
            {"stem": "A farmer has 100 feet of fencing. She wants to enclose the largest possible circular area. What area can she enclose? Explain why a circle gives more area than a square with the same perimeter.", "answer": "C = 100 → r = 100/(2π) ≈ 15.92 ft → A = π(15.92²) ≈ 795.8 ft². Square: side = 25, area = 625 ft². Circle wins because it has the highest area-to-perimeter ratio of any shape.", "hint": ""},
            {"stem": "Design a pizza pricing system for three sizes: Small (8\" diameter), Medium (12\" diameter), Large (16\" diameter). If the small costs $8, what should the medium and large cost if priced proportionally by area? Is this how real pizza shops price? Why or why not?", "answer": "Small area = 50.3 in², Medium = 113.1 in², Large = 201.1 in². Ratios: Med is 2.25× small, Large is 4× small. Fair prices: Med = $18, Large = $32. Real shops charge less because of competition and fixed costs.", "hint": ""},
            {"stem": "Two semicircles are drawn on opposite sides of a 10-inch line segment (one above, one below), with the segment as their diameters. A full circle with diameter 10 inches is drawn centered on the segment. Describe the resulting shape and find the area of ONLY the regions inside the semicircles but outside the circle.", "answer": "The overlapping regions cancel out due to symmetry. The area inside semicircles but outside the circle equals the area inside the circle but outside the semicircles. Net difference = 0. Total combined area of both semicircles = π(5²) = same as circle.", "hint": ""},
        ],
    },
    "circumference": {
        "beginning": [
            {"stem": "A circle has a diameter of {d} cm. What is the circumference? Use C = πd.", "answer": "C = π × {d} = {c_val} cm", "hint": "Multiply the diameter by π (≈ 3.14)"},
            {"stem": "A bicycle wheel has a radius of 13 inches. What is the circumference?", "answer": "d = 26 in, C = π × 26 ≈ 81.7 inches", "hint": "First double the radius to get diameter, then multiply by π"},
            {"stem": "Match: C = πd measures the _____ of a circle.\n(a) area  (b) distance around  (c) distance across", "answer": "(b) distance around", "hint": "Circumference = the perimeter of a circle"},
        ],
        "partial": [
            {"stem": "A circular track has a circumference of 400 meters. What is the diameter of the track?", "answer": "d = C ÷ π = 400 ÷ π ≈ 127.3 meters", "hint": "Rearrange C = πd to solve for d"},
            {"stem": "A wheel rolls exactly 5 full rotations and covers 94.2 inches. What is the radius of the wheel?", "answer": "One rotation = 94.2 ÷ 5 = 18.84 in = C, d = 18.84 ÷ π ≈ 6, r = 3 inches", "hint": "One rotation = one circumference"},
            {"stem": "Compare: Which is longer — the circumference of a circle with radius 7 or the perimeter of a square with side 11?", "answer": "Circle: C = 2π(7) = 44.0. Square: P = 4(11) = 44. They are approximately equal!", "hint": "Calculate both and compare"},
        ],
        "proficient": [
            {"stem": "A dog is tied to a stake with a 15-foot leash. How much ground can the dog walk around the full circle? If the leash is lengthened by 5 feet, how much more walking distance does the dog gain?", "answer": "Original C = 2π(15) = 94.2 ft. New C = 2π(20) = 125.7 ft. Gain = 31.4 ft", "hint": ""},
            {"stem": "Earth's equator is approximately 24,901 miles. Estimate Earth's diameter. If you added 10 feet to a rope around the equator, how high above the surface would it float?", "answer": "d ≈ 24,901 ÷ π ≈ 7,926 miles. Extra rope: 10 ft added to C means Δr = 10/(2π) ≈ 1.6 ft — surprisingly, just over 19 inches above the surface!", "hint": ""},
            {"stem": "A semicircular window has a flat edge of 3 feet. What is the total perimeter of the window (curved part + flat edge)?", "answer": "Diameter = 3, so curved part = πd/2 = 3π/2 ≈ 4.71 ft. Total = 4.71 + 3 = 7.71 ft", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Explain to a friend why the ratio of circumference to diameter is ALWAYS the same number (π), no matter the size of the circle. Use at least two different-sized circles as evidence.", "answer": "Every circle is similar (same shape, scaled). If you double the diameter, you double the circumference, so C/d stays constant. Example: d=2 → C=6.28, d=10 → C=31.4. Both give C/d ≈ 3.14. This constant ratio IS π.", "hint": ""},
            {"stem": "A running track is 400m around. It has two straight sections (100m each) and two semicircular ends. What is the width of the track (diameter of the semicircles)? If a runner in the outside lane (1.2m wider) runs the same shape, how much farther do they run?", "answer": "Curved portion = 400 - 200 = 200m = full circle C. d = 200/π ≈ 63.7m. Outer lane: d₂ = 63.7 + 2(1.2) = 66.1m. Outer C = π(66.1) = 207.6m. Outer total = 207.6 + 200 = 407.6m. Extra = 7.6m per lap.", "hint": ""},
            {"stem": "Create your own real-world problem that requires finding circumference. Your problem must involve a situation where someone would actually NEED to know the distance around a circle (not just a textbook exercise). Solve it and explain why circumference matters in your scenario.", "answer": "Open-ended. Example: 'How much LED strip lighting do I need to wrap around a circular mirror with a 24-inch diameter?' C = π(24) ≈ 75.4 inches. Buy 76+ inches. Circumference matters because you're physically wrapping something around a circle.", "hint": ""},
        ],
    },
    "proportional relationships": {
        "beginning": [
            {"stem": "If 3 notebooks cost $6, how much do 6 notebooks cost?", "answer": "$12 (double the notebooks = double the cost)", "hint": "If you buy twice as many, you pay twice as much"},
            {"stem": "A recipe uses 2 cups of flour for 12 cookies. Complete the table:\n| Flour | Cookies |\n| 2 | 12 |\n| 4 | ? |\n| 6 | ? |", "answer": "4 cups → 24 cookies, 6 cups → 36 cookies", "hint": "Find the pattern: multiply flour by 6 to get cookies"},
            {"stem": "Is this proportional? x: 1,2,3,4 and y: 5,10,15,20. How do you know?", "answer": "Yes — y/x = 5 every time (constant ratio)", "hint": "Divide y by x for each pair. If the answer is always the same, it's proportional."},
        ],
        "partial": [
            {"stem": "A car travels 180 miles in 3 hours at a constant speed. Write an equation relating distance (d) and time (t). How far in 7 hours?", "answer": "Rate = 180 ÷ 3 = 60 mph. d = 60t. At 7 hrs: d = 60(7) = 420 miles", "hint": "Find the unit rate first (distance per 1 hour)"},
            {"stem": "Graph shows a straight line through (0,0) and (4,12). Is this proportional? What is the constant of proportionality? Write the equation.", "answer": "Yes (line through origin). k = 12/4 = 3. Equation: y = 3x", "hint": "Proportional relationships always pass through the origin"},
            {"stem": "Store A: 5 apples for $3. Store B: 8 apples for $5. Which is the better deal?", "answer": "Store A: $0.60/apple. Store B: $0.625/apple. Store A is cheaper per apple.", "hint": "Find the price per 1 apple at each store"},
        ],
        "proficient": [
            {"stem": "Marcus earns $12/hour. Jayla earns $15/hour. Both start saving at the same time. Graph both relationships on the same axes. After how many hours will Jayla have earned $45 more than Marcus?", "answer": "Marcus: y = 12x, Jayla: y = 15x. Difference = 3x. When 3x = 45, x = 15 hours.", "hint": ""},
            {"stem": "A scale drawing uses 1 inch = {scale} feet. A room measures 3.5 inches by 4 inches on the drawing. Find the actual area of the room in square feet.", "answer": "Actual: 3.5 × {scale} by 4 × {scale} feet. Area = (3.5 × {scale}) × (4 × {scale}) sq ft", "hint": ""},
            {"stem": "Water flows into a tank at a rate of 3 gallons per minute. The tank already has 20 gallons. Is the TOTAL amount of water proportional to time? Why or why not?", "answer": "No — the equation is y = 3x + 20, which doesn't pass through the origin. The relationship is LINEAR but not proportional because of the starting amount.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "A phone plan charges $0.05 per text message plus a $10 monthly fee. A second plan charges $0.08 per text with no monthly fee. For what number of messages are the costs equal? Explain which plan is proportional and why the other is not. Create a graph showing both plans.", "answer": "Plan 1: C = 0.05m + 10 (not proportional — doesn't go through origin). Plan 2: C = 0.08m (proportional). Equal when 0.05m + 10 = 0.08m → 10 = 0.03m → m ≈ 333 texts. Below 333: Plan 2 cheaper. Above 333: Plan 1 cheaper.", "hint": ""},
            {"stem": "Create two real-world scenarios: one that IS proportional and one that LOOKS proportional but isn't. Explain the key mathematical difference. Include tables, equations, and graphs for both.", "answer": "Open-ended. Key insight: proportional must pass through (0,0) and have constant y/x ratio. Example: Proportional — miles per gallon at constant rate. Not proportional — taxi fare (starts with base fare + rate per mile).", "hint": ""},
            {"stem": "A painter mixes blue and yellow paint in a 2:5 ratio to make green. She has 8 cups of blue and 15 cups of yellow. What is the MAXIMUM amount of green paint she can make? How much of which color will be left over? If she wanted to use ALL of both colors, what ratio would she need?", "answer": "Blue limits: 8 cups blue needs 20 cups yellow (only has 15). Yellow limits: 15 cups yellow needs 6 cups blue. Max green: 6 + 15 = 21 cups. Leftover: 2 cups blue. To use all: ratio would be 8:15.", "hint": ""},
        ],
    },
    "distance rate time": {
        "beginning": [
            {"stem": "A car drives 60 miles per hour for 3 hours. How far does it go?", "answer": "d = r × t = 60 × 3 = 180 miles", "hint": "Distance = Rate × Time"},
            {"stem": "A train travels 200 miles in 4 hours. What is its speed?", "answer": "Rate = d ÷ t = 200 ÷ 4 = 50 mph", "hint": "Speed = Distance ÷ Time"},
            {"stem": "Fill in: d = ___ × ___", "answer": "d = rate × time", "hint": "The distance formula uses speed and time"},
        ],
        "partial": [
            {"stem": "Two towns are 300 miles apart. A bus leaves Town A at 50 mph. How long to reach Town B?", "answer": "t = d ÷ r = 300 ÷ 50 = 6 hours", "hint": "Rearrange: Time = Distance ÷ Rate"},
            {"stem": "A cyclist rides 12 miles in 45 minutes. What is their speed in miles per hour?", "answer": "45 min = 0.75 hours. Speed = 12 ÷ 0.75 = 16 mph", "hint": "Convert minutes to hours first (divide by 60)"},
            {"stem": "Graph the distance over time for a car going 40 mph. Plot points at t = 0, 1, 2, 3, 4 hours.", "answer": "Points: (0,0), (1,40), (2,80), (3,120), (4,160). Straight line through origin.", "hint": "At each hour, multiply time × 40"},
        ],
        "proficient": [
            {"stem": "Car A leaves Chicago heading east at 55 mph. Car B leaves Chicago 1 hour later heading east at 70 mph. When does Car B catch up?", "answer": "After 1 hr, Car A is 55 mi ahead. Gap closes at 70-55 = 15 mph. Time = 55 ÷ 15 ≈ 3.67 hrs after B leaves (4.67 hrs after A).", "hint": ""},
            {"stem": "A round trip: you drive to a store 30 miles away at 60 mph, shop for 30 minutes, then drive home at 40 mph. What is your average speed for the entire trip (including shopping)?", "answer": "To store: 30/60 = 0.5 hr. Shopping: 0.5 hr. Return: 30/40 = 0.75 hr. Total time: 1.75 hr. Total distance: 60 mi. Avg speed = 60/1.75 ≈ 34.3 mph", "hint": ""},
            {"stem": "A delivery drone flies 5 miles at 30 mph, then 10 miles at 60 mph. What is the average speed for the whole trip?", "answer": "Time₁ = 5/30 = 1/6 hr. Time₂ = 10/60 = 1/6 hr. Total: 15 mi in 2/6 hr = 15 ÷ 0.333 = 45 mph. NOT simply (30+60)/2 = 45 (coincidence here, but method matters).", "hint": ""},
        ],
        "exemplary": [
            {"stem": "George sees a lightning flash and hears thunder 4 seconds later. Sound travels about 1,100 ft/sec, light travels 186,000 mi/sec. How far away was the lightning? Why can we ignore the time it takes light to travel? Express your answer in both feet and miles.", "answer": "d = 1100 × 4 = 4,400 ft ≈ 0.83 miles. Light time: 0.83/186,000 ≈ 0.0000045 sec — essentially instant compared to 4 seconds. This is why we only time the sound.", "hint": ""},
            {"stem": "Design a training plan for a runner preparing for a 10K (6.2 miles). They currently run at 12 min/mile and want to reach 9 min/mile in 8 weeks. Create a proportional weekly speed progression and calculate total training time saved per run at goal pace.", "answer": "Open-ended. Current: 6.2 × 12 = 74.4 min. Goal: 6.2 × 9 = 55.8 min. Savings = 18.6 min. Weekly pace decrease: 3 min ÷ 8 = 0.375 min/mile per week.", "hint": ""},
            {"stem": "Two ships leave port at the same time. Ship A heads north at 20 knots, Ship B heads east at 15 knots. After 2 hours, how far apart are they? At what rate is the distance between them increasing? (Hint: think about what shape their paths create.)", "answer": "After 2 hrs: A is 40 nm north, B is 30 nm east. They form a right triangle. Distance = √(40² + 30²) = √2500 = 50 nm. Rate of separation = 50/2 = 25 knots (by Pythagorean relationship, this is √(20² + 15²) = 25).", "hint": ""},
        ],
    },
    "pi": {
        "beginning": [
            {"stem": "What is π (pi) approximately equal to? Choose: (a) 3.14  (b) 4.13  (c) 2.71", "answer": "(a) π ≈ 3.14", "hint": "Pi starts with 3.14..."},
            {"stem": "A circle has diameter 10. Multiply the diameter by π. What did you find?", "answer": "10 × 3.14 = 31.4 — this is the circumference!", "hint": "Multiplying diameter by π gives circumference"},
            {"stem": "True or False: π is the ratio of a circle's circumference to its diameter.", "answer": "True. C ÷ d = π for every circle.", "hint": "Pi is defined as circumference divided by diameter"},
        ],
        "partial": [
            {"stem": "Measure 5 circular objects. Record diameter and circumference. Divide C by d for each. What do you notice?", "answer": "Every ratio should be close to 3.14 (π). Small differences are measurement error.", "hint": "The ratio C/d should be approximately the same for all circles"},
            {"stem": "Is π rational or irrational? How do you know?", "answer": "Irrational — its decimal never terminates or repeats. It cannot be written as a fraction of two integers.", "hint": "Rational numbers can be written as a/b where a and b are integers"},
            {"stem": "If you know C = 2πr and A = πr², rewrite both formulas using d (diameter) instead of r.", "answer": "Since r = d/2: C = πd, A = π(d/2)² = πd²/4", "hint": "Replace every r with d/2"},
        ],
        "proficient": [
            {"stem": "Ancient mathematicians estimated π: Archimedes said 22/7, Chinese mathematicians used 355/113. Calculate the decimal for each. Which is closer to π = 3.14159265...?", "answer": "22/7 = 3.142857... (off by 0.0013). 355/113 = 3.1415929... (off by 0.0000003). 355/113 is remarkably more accurate.", "hint": ""},
            {"stem": "A wheel has circumference C. Write an expression for the number of complete rotations needed to travel 1 mile (5,280 feet). If C = 7 feet, how many rotations?", "answer": "Rotations = 5280/C. If C = 7: 5280/7 ≈ 754.3 rotations.", "hint": ""},
            {"stem": "Explain why π shows up in BOTH the circumference formula AND the area formula. What does it have to do with circles specifically?", "answer": "π is fundamentally the ratio C/d. Area can be derived by 'unwrapping' a circle into triangles — the base of all triangles combined equals C = 2πr, and height = r, so A = ½ × 2πr × r = πr².", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Research: Describe THREE different methods humans have used throughout history to calculate π. For each method, explain the mathematical idea behind it and how accurate it was.", "answer": "Examples: (1) Archimedes' polygon method (inscribed/circumscribed polygons, 96-sided → 3.1408-3.1429), (2) Infinite series like Leibniz: π/4 = 1 - 1/3 + 1/5 - 1/7..., (3) Monte Carlo method (random points in square, ratio inside circle ≈ π/4).", "hint": ""},
            {"stem": "Pi Day is March 14 (3/14). Design a mathematical investigation that proves π exists — that is, prove that C/d is the same for ALL circles, regardless of size. Your proof should be convincing to a classmate.", "answer": "Open-ended. Key insight: all circles are similar. If circle B has diameter k× circle A's diameter, then B's circumference is also k× A's circumference (scaling preserves ratios). Therefore C/d is invariant under scaling → it's a universal constant.", "hint": ""},
            {"stem": "A mathematician claims: 'π is wrong — we should use τ (tau) = 2π instead, because τ is the ratio of circumference to RADIUS, which is more natural.' Evaluate this claim. Rewrite C, A, and the unit circle using τ. Do you agree? Make a mathematical argument.", "answer": "With τ: C = τr (simpler!), A = ½τr² (like ½bh for triangle), full circle = τ radians (one full turn). Arguments for τ: more elegant in trig, full turn = τ. Arguments for π: tradition, A = πr² is cleaner. Mathematical substance is identical — it's a notational debate.", "hint": ""},
        ],
    },
    "integer operations": {
        "beginning": [
            {"stem": "Calculate: {a} + {b} where {a} is positive and {b} is positive.", "answer": "{a} + {b} = {sum}", "hint": "When both numbers are positive, add them normally"},
            {"stem": "A bank account shows a balance of -$150 (overdrawn). You deposit $100. What is your new balance?", "answer": "-150 + 100 = -$50", "hint": "Moving right on the number line from -150"},
            {"stem": "True or False: {neg} × {pos} gives a negative result.", "answer": "True. A negative times a positive is always negative.", "hint": "Positive × Negative = Negative"},
        ],
        "partial": [
            {"stem": "Simplify: {neg1} + {neg2} + {pos}", "answer": "{neg1} + {neg2} + {pos} = {result}", "hint": "Combine the negatives first, then add the positive"},
            {"stem": "Evaluate: {neg} - {pos}. What is the result?", "answer": "{neg} - {pos} = {result}", "hint": "Subtracting a positive moves left on the number line"},
            {"stem": "A scuba diver is at -40 feet. She descends another 15 feet. Where is she now?", "answer": "-40 - 15 = -55 feet", "hint": "Going deeper (more negative) means subtract from the negative"},
        ],
        "proficient": [
            {"stem": "Simplify: ({neg1} + {pos}) × {neg2}", "answer": "({neg1} + {pos}) × {neg2} = {inter} × {neg2} = {result}", "hint": ""},
            {"stem": "A football team loses 5 yards on first down, gains 12 yards on second down, then loses 3 yards on third down. What is the net yardage change?", "answer": "-5 + 12 - 3 = 4 yards gained", "hint": ""},
            {"stem": "Evaluate: {neg1} × {neg2} ÷ {pos}. Explain why the result is positive.", "answer": "{neg1} × {neg2} = {prod}, then {prod} ÷ {pos} = {result}. Negative × Negative = Positive.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "A company's profit changes over four quarters: Q1: +$50K, Q2: -$20K, Q3: +$30K, Q4: -$15K. Calculate the annual profit. If the company wants to triple Q1's profit next year and halve Q4's loss, what would the new annual target be?", "answer": "Total: 50 - 20 + 30 - 15 = $45K. If Q1 becomes $150K and Q4 becomes -$7.5K, new target would increase by (150-50) + (-7.5-(-15)) = $107.5K, giving $45K + $107.5K = $152.5K.", "hint": ""},
            {"stem": "Prove that a negative number times a negative number always gives a positive. Use a real-world context (like owing debt) to explain your reasoning.", "answer": "Debt example: If I owe $5 (negative) to 3 people, I owe $15 total (negative × positive = negative). If I owe $5 to someone, and that debt is canceled/removed (negative × negative), I gain $5 (positive). Algebraic: -5 × -3 = 5 × 3 = 15 by the pattern of opposites.", "hint": ""},
            {"stem": "Create a table showing all combinations of operations {+, -, ×, ÷} applied to a positive and negative number. Predict the sign of each result, then verify with specific examples. Write a rule for each operation.", "answer": "Addition: + with + gives +, - with - gives -, +/- depends on magnitude. Subtraction: flips the sign of what's subtracted. Multiplication: same sign = positive, different signs = negative. Division: same rules as multiplication.", "hint": ""},
        ],
    },
    "absolute value": {
        "beginning": [
            {"stem": "What is the absolute value of -7? Hint: it's the distance from 0.", "answer": "|-7| = 7", "hint": "Absolute value is always positive — it's how far from zero"},
            {"stem": "Find: |{num}|", "answer": "|{num}| = {abs}", "hint": "Distance from zero, always positive"},
            {"stem": "Which is greater: |-5| or |3|?", "answer": "|-5| = 5, |3| = 3, so |-5| is greater", "hint": "Compare the absolute values as positive numbers"},
        ],
        "partial": [
            {"stem": "Solve: |x| = 8. What are the possible values of x?", "answer": "x = 8 or x = -8 (both are 8 units from zero)", "hint": "Think of two points on the number line that are distance 8 from 0"},
            {"stem": "The temperature was 5°F in the morning and -3°F in the evening. Which was colder? Which has a larger absolute value?", "answer": "-3°F is colder (lower temperature). |-3| = 3, |5| = 5, so 5°F has larger absolute value.", "hint": "Colder doesn't mean larger absolute value"},
            {"stem": "Simplify: |{neg}| + |{pos}|", "answer": "|{neg}| + |{pos}| = {abs1} + {abs2} = {sum}", "hint": "Find the absolute value of each, then add"},
        ],
        "proficient": [
            {"stem": "Graph on a number line: all values of x where |x| < 4. Describe your answer as an inequality.", "answer": "-4 < x < 4. Points between -4 and 4 are less than 4 units from zero.", "hint": ""},
            {"stem": "A submarine is 500 meters below sea level. A satellite is 400 meters above sea level. What is the absolute value of their distance? Who is farther from sea level?", "answer": "Submarine: -500, satellite: +400. Distance = |−500 − (+400)| = |-900| = 900 meters. Submarine is farther from sea level (|−500| = 500 > 400).", "hint": ""},
            {"stem": "Solve: |x - 3| = 5. Find all solutions and verify.", "answer": "x - 3 = 5 → x = 8, or x - 3 = -5 → x = -2. Check: |8-3| = 5 ✓, |-2-3| = |-5| = 5 ✓", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Two factories emit pollution. Factory A is 120 units away from a reference point (in one direction), Factory B is 150 units away (in the opposite direction). Using absolute value, explain how far they are from each other. Then explain why absolute value is the right tool here.", "answer": "If positions are 120 and -150, distance = |120 - (-150)| = |270| = 270 units. Absolute value is right because it measures physical distance regardless of direction.", "hint": ""},
            {"stem": "Prove or disprove: For any real numbers a and b, |a + b| = |a| + |b|. Give an example where it's true and one where it's false. When is this equation true?", "answer": "False in general. Example: |3 + (-5)| = |-2| = 2, but |3| + |-5| = 3 + 5 = 8. True when a and b have the same sign: |3 + 4| = |7| = 7 and |3| + |4| = 7. True when one is 0.", "hint": ""},
            {"stem": "Create a real-world problem where you must use absolute value to find distance, and another where you must solve an absolute value equation. Solve both and explain why absolute value was necessary.", "answer": "Open-ended. Distance: 'Cities at coordinates 50 and -30 miles — how far apart?' Equation: 'GPS shows me 20 units from home — where am I?' Both use absolute value for direction-independent magnitude.", "hint": ""},
        ],
    },
    "equivalent expressions": {
        "beginning": [
            {"stem": "Use the distributive property: 3(x + 2) = ?", "answer": "3(x + 2) = 3x + 6", "hint": "Multiply 3 times each term inside the parentheses"},
            {"stem": "Combine like terms: 5x + 3x = ?", "answer": "5x + 3x = 8x", "hint": "Add the coefficients of the same variable"},
            {"stem": "Simplify: 4y + 2 + 3y + 5 = ?", "answer": "7y + 7", "hint": "Group the y terms together, then the numbers"},
        ],
        "partial": [
            {"stem": "Expand and simplify: 2(x + 3) + 4(x - 1)", "answer": "2x + 6 + 4x - 4 = 6x + 2", "hint": "Distribute first, then combine like terms"},
            {"stem": "Are 3(2x + 4) and 6x + 12 equivalent? Show your work.", "answer": "Yes. 3(2x + 4) = 6x + 12. Both expressions are identical.", "hint": "Distribute the 3 and check if you get the same result"},
            {"stem": "Simplify: -2(a - 3) + 5a", "answer": "-2a + 6 + 5a = 3a + 6", "hint": "Remember: -2 times -3 becomes +6"},
        ],
        "proficient": [
            {"stem": "Simplify: 2(3x - 5) + 3(2x + 4) - 6. Show that your answer is equivalent by evaluating both the original and simplified form when x = 2.", "answer": "Original: 6x - 10 + 6x + 12 - 6 = 12x - 4. When x = 2: Original = 2(3(2)-5) + 3(2(2)+4) - 6 = 2(1) + 3(8) - 6 = 20. Simplified: 12(2) - 4 = 20 ✓", "hint": ""},
            {"stem": "A rectangle has length (2x + 3) and width (x - 1). Write the perimeter as a simplified expression. If x = 5, what is the perimeter?", "answer": "P = 2[(2x+3) + (x-1)] = 2(3x+2) = 6x + 4. When x=5: P = 6(5) + 4 = 34 units.", "hint": ""},
            {"stem": "Factor: 6x + 9. What expression, when distributed, gives 6x + 9? Is this the same as the distributive property in reverse?", "answer": "6x + 9 = 3(2x + 3). Yes, factoring is the reverse of distributive property — finding the common factor.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Write two different equivalent expressions for the area of an L-shaped figure (think of a large rectangle with a rectangular piece cut from one corner). Prove they're equivalent by simplifying.", "answer": "Large rectangle: 10 × 8 = 80. Cut piece: 3 × 2 = 6. Method 1: 80 - 6 = 74. Method 2: (10-3) × 8 + 3 × (8-2) = 7(8) + 3(6) = 56 + 18 = 74. Algebraically equivalent.", "hint": ""},
            {"stem": "Explain why 2(3x + 5) and 6x + 5 are NOT equivalent. Then explain how you could change one of them to make them equivalent. How many different ways can you fix it?", "answer": "2(3x+5) = 6x+10, not 6x+5. Difference is 5. Could change: (1) Second to 6x+10, (2) First to 2(3x+2.5) = 6x+5, (3) Factor 6x+10 as 2(3x+5), etc. Shows deep understanding of equivalence.", "hint": ""},
            {"stem": "A student writes: 3(x+2) = 3x + 2. Identify the error. Create three more problems where students commonly make the same mistake. Explain the conceptual misunderstanding.", "answer": "Error: didn't distribute the 3 to the 2. Misconception: thinks distributive property only applies to variables. Common mistakes: 2(a+4)=2a+4, 5(b-3)=5b-3, 4(2c+1)=4(2c)+1. All fail to multiply BOTH terms in parentheses.", "hint": ""},
        ],
    },
    "equations": {
        "beginning": [
            {"stem": "Solve: x + 5 = 12", "answer": "x = 7", "hint": "What number plus 5 equals 12?"},
            {"stem": "Solve: 3x = 15", "answer": "x = 5", "hint": "Divide both sides by 3"},
            {"stem": "Which equation has x = 2 as the solution?\n(a) x + 3 = 5  (b) 2x = 5  (c) x - 1 = 0", "answer": "(a) x + 3 = 5. Check: 2 + 3 = 5 ✓", "hint": "Substitute x = 2 into each equation"},
        ],
        "partial": [
            {"stem": "Solve: 2x + 3 = 11", "answer": "2x = 8, x = 4", "hint": "Subtract 3 first, then divide by 2"},
            {"stem": "Solve: 4x - 7 = 9. Show each step.", "answer": "4x = 16, x = 4", "hint": "Add 7 to both sides, then divide by 4"},
            {"stem": "The perimeter of a square is 20 cm. Write an equation for the side length s, then solve it.", "answer": "4s = 20, s = 5 cm", "hint": "Perimeter of a square = 4 × side length"},
        ],
        "proficient": [
            {"stem": "Solve: 3(x + 2) = 18. Verify your answer by substituting back.", "answer": "3x + 6 = 18, 3x = 12, x = 4. Check: 3(4+2) = 3(6) = 18 ✓", "hint": ""},
            {"stem": "A phone plan costs $40 per month plus $0.10 per text. If your bill is $47, write and solve an equation for the number of texts (t).", "answer": "40 + 0.10t = 47, 0.10t = 7, t = 70 texts", "hint": ""},
            {"stem": "Solve: 5 - 2x = 11. What is x? Interpret this equation in the context of a game where 5 is a starting score.", "answer": "5 - 2x = 11 → -2x = 6 → x = -3. In game context: you lost 2 points per round for -3 rounds = 6 points, ending at 5 - 6 = -1... Context matters for interpretation.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Write an equation that models this: Marcus had some money. He spent half of it on a concert ticket, then spent $15 on dinner. He has $35 left. Solve for his original amount. Then modify the problem so he EARNED money instead of spent money.", "answer": "Original: x/2 - 15 = 35 → x/2 = 50 → x = $100. Modified: x/2 + 15 = 35 → x = 40. Shows how equation structure changes with context.", "hint": ""},
            {"stem": "Explain why 2x + 3 = 11 and 2x = 8 are equivalent equations. What property allows you to subtract 3 from both sides? Give a real-world analogy with a balanced scale.", "answer": "Subtraction property of equality: if a = b, then a - c = b - c. Scale analogy: if scale balances at 11 units, removing 3 units from both sides keeps it balanced. These are equivalent equations because they have the same solution.", "hint": ""},
            {"stem": "Create an equation that requires AT LEAST 4 steps to solve, where the variable appears on BOTH sides of the equation. Solve it completely and explain each step's purpose.", "answer": "Example: 3x + 5 = x + 17. Step 1: Collect variables: 3x - x = 17 - 5 (subtract x, subtract 5). Step 2: 2x = 12. Step 3: x = 6. Step 4: Verify: 3(6)+5 = 23, 6+17 = 23 ✓", "hint": ""},
        ],
    },
    "inequalities": {
        "beginning": [
            {"stem": "Is 5 a solution to x > 3? Explain.", "answer": "Yes, because 5 > 3 is true.", "hint": "Check: does the number satisfy the inequality?"},
            {"stem": "Write an inequality for: x is at least 10.", "answer": "x ≥ 10", "hint": "'At least' means greater than or equal to"},
            {"stem": "Graph on a number line: x < 4. Use a circle and arrow to show all solutions.", "answer": "Open circle at 4, arrow pointing left", "hint": "Open circle for < or >, closed circle for ≤ or ≥"},
        ],
        "partial": [
            {"stem": "Solve: x + 3 < 8", "answer": "x < 5", "hint": "Subtract 3 from both sides, like solving equations"},
            {"stem": "Solve: 2x ≥ 10. Graph the solution on a number line.", "answer": "x ≥ 5. Closed circle at 5, arrow pointing right", "hint": "Divide both sides by 2"},
            {"stem": "A movie is appropriate for ages 13 and older. Write an inequality for the age (a). If you're 12, can you watch it?", "answer": "a ≥ 13. No, 12 does not satisfy the inequality.", "hint": "'And older' means greater than or equal to"},
        ],
        "proficient": [
            {"stem": "Solve: 3x - 5 > 10. Graph and describe the solution in words.", "answer": "3x > 15, x > 5. All numbers greater than 5 satisfy the inequality.", "hint": ""},
            {"stem": "A bakery has a budget of $200 for ingredients. Flour costs $3 per bag and sugar costs $5 per bag. If they buy 20 bags of flour, how many bags of sugar (s) can they afford? Write and solve an inequality.", "answer": "3(20) + 5s ≤ 200 → 60 + 5s ≤ 200 → 5s ≤ 140 → s ≤ 28. They can afford at most 28 bags of sugar.", "hint": ""},
            {"stem": "Solve 4x - 3 ≤ 9 and graph it. Is x = 2.5 a solution? Is x = 3.1? Verify both.", "answer": "4x ≤ 12, x ≤ 3. Check x=2.5: 4(2.5)-3 = 7 ≤ 9 ✓. Check x=3.1: 4(3.1)-3 = 9.4 ≤ 9? No ✗", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Create a compound inequality (two inequalities combined with 'and' or 'or'). Example: find all x where 2 < x ≤ 5. Solve it, graph it, and explain when you'd use a compound inequality in real life.", "answer": "A child's height must be between 40 and 60 inches to ride a roller coaster: 40 ≤ h ≤ 60. Graph: closed circle at 40, closed at 60, shaded between. This is more efficient than two separate inequalities.", "hint": ""},
            {"stem": "A musician earns $50 per event plus $2 per person who attends. To keep a profit, she needs to earn more than $150 per event. Write and solve an inequality for the minimum attendance. What if the venue charges a $30 fee? How does that change the inequality?", "answer": "Original: 50 + 2a > 150 → a > 50 (need 51+ people). With fee: 50 + 2a - 30 > 150 → 20 + 2a > 150 → a > 65 (need 66+ people). Fee increases minimum attendance by 15 people.", "hint": ""},
            {"stem": "Explain why multiplying or dividing an inequality by a negative number FLIPS the inequality sign. Use -2x > 8 as your example, then create another example where this rule matters in a real-world context.", "answer": "When dividing 8 by -2: -2x > 8 → x < -4 (flipped because -2 is negative). Real world: 'Score is more than 20 points behind my opponent' (-score > -20) means my opponent's lead is less than 20 points (lead < 20). Flipping reflects the reversal in perspective.", "hint": ""},
        ],
    },
    "percent": {
        "beginning": [
            {"stem": "What is 10% of 50?", "answer": "0.10 × 50 = 5", "hint": "Percent means per 100. 10% = 0.10"},
            {"stem": "A jacket originally costs $80 and is on sale for 25% off. How much is the discount?", "answer": "0.25 × $80 = $20 discount", "hint": "Find 25% of the original price"},
            {"stem": "If 20% of a number is 30, what is the number? (Hint: use 0.20 × ? = 30)", "answer": "30 ÷ 0.20 = 150", "hint": "Divide the part by the percent to find the whole"},
        ],
        "partial": [
            {"stem": "A shirt costs $40. With a 15% discount and 8% tax, what is the final price?", "answer": "Discount: 0.15 × $40 = $6. Sale price: $34. Tax: 0.08 × $34 = $2.72. Final: $36.72", "hint": "Apply discount first, then calculate tax on the reduced price"},
            {"stem": "Last year, a store sold 500 items. This year, they sold 750 items. What is the percent increase?", "answer": "Change = 750 - 500 = 250. Percent increase = (250 ÷ 500) × 100% = 50%", "hint": "Percent change = (new - old) ÷ old × 100%"},
            {"stem": "A restaurant bill is $45 before tip. You want to leave a 18% tip. How much total will you pay?", "answer": "Tip = 0.18 × $45 = $8.10. Total = $45 + $8.10 = $53.10", "hint": "Find the tip amount, then add it to the original bill"},
        ],
        "proficient": [
            {"stem": "A video game costs $60. During a 20% off sale, you get an additional $5 coupon. If tax is 7%, what do you pay? What is the final percent discount from the original?", "answer": "20% off: $60 - 12 = $48. Coupon: $48 - $5 = $43. Tax: $43 × 0.07 = $3.01. Total: $46.01. Final discount: 1 - 46.01/60 = 23.3%", "hint": ""},
            {"stem": "A population grew from 8,000 to 9,200 people. Calculate the percent increase. If growth continues at the same rate, what will the population be next year?", "answer": "Increase = 9,200 - 8,000 = 1,200. Percent: (1,200 ÷ 8,000) × 100% = 15%. Next year: 9,200 × 1.15 = 10,580 people", "hint": ""},
            {"stem": "A phone price decreased from $800 to $640. What is the percent decrease? The next month, the price increased 10% from $640. Is the final price equal to the original? Why or why not?", "answer": "Decrease: (160 ÷ 800) × 100% = 20%. After 10% increase: $640 × 1.10 = $704. No, final ≠ original. Same percent of different bases gives different amounts.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Compare two cell phone plans: Plan A costs $30/month with unlimited data; Plan B costs $15/month but charges $0.05 per MB of data. If you use 600 MB per month, which is cheaper? What percent savings does the better plan offer? Create a comparison showing when each plan becomes better.", "answer": "Plan A: $30. Plan B: $15 + (600 × 0.05) = $15 + $30 = $45. Plan A is cheaper by $15, which is 33% savings on Plan B's price. Breakeven: 15 + 0.05m = 30 → m = 300 MB. Plan A better for high usage.", "hint": ""},
            {"stem": "A store marks up wholesale prices by 150% to get retail price. Then they discount items by 40% for a sale. If an item cost $20 wholesale, what is the final sale price? What overall percent change is this from wholesale? Is markup percentage equal to discount percentage in reverse?", "answer": "Retail: $20 × 2.50 = $50 (150% markup = 250% of original). Sale: $50 × 0.60 = $30. Overall: ($30-$20)/$20 = 50% markup from wholesale. Markups and discounts don't work symmetrically because they apply to different base amounts.", "hint": ""},
            {"stem": "Create a real-world scenario where understanding percent is CRITICAL for making a good decision (e.g., comparing loans, investment returns, discount deals). Solve it completely and explain what percentage comparison reveals that just looking at dollar amounts would hide.", "answer": "Open-ended. Example: Two loans: A charges 5% interest on $10,000; B charges 8% on $5,000. Dollar amounts: A = $500, B = $400 interest. But as percent of loan: A = 5% vs B = 8%, showing B is actually more expensive proportionally even with less total interest.", "hint": ""},
        ],
    },
    "similarity": {
        "beginning": [
            {"stem": "Two triangles are similar. Triangle A has sides 3, 4, 5. Triangle B has sides 6, 8, 10. What is the scale factor?", "answer": "Scale factor = 2 (each side of B is 2 times the side of A)", "hint": "Divide a side of the larger triangle by the corresponding side of the smaller"},
            {"stem": "Similar figures have the same ____ but different ____.", "answer": "Same: shape (or angles). Different: size", "hint": "Similar means same shape, different size"},
            {"stem": "A map has a scale of 1 inch = 5 miles. If two cities are 3 inches apart on the map, how far apart are they in reality?", "answer": "3 × 5 = 15 miles", "hint": "Multiply the map distance by the scale factor"},
        ],
        "partial": [
            {"stem": "Rectangle A has dimensions 4 by 6. Rectangle B is similar with length 9. What is its width?", "answer": "Scale factor = 9 ÷ 6 = 1.5. Width = 4 × 1.5 = 6", "hint": "Find the scale factor using the known sides, then apply it"},
            {"stem": "A model car is 1:24 scale. If the model is 5 inches long, how long is the actual car in feet?", "answer": "Actual = 5 × 24 = 120 inches = 10 feet", "hint": "Scale 1:24 means actual is 24 times the model"},
            {"stem": "Two similar pentagons have a scale factor of 3. If the smaller pentagon has a perimeter of 15 cm, what is the perimeter of the larger pentagon?", "answer": "Perimeter of larger = 15 × 3 = 45 cm", "hint": "Perimeter scales by the same factor as the sides"},
        ],
        "proficient": [
            {"stem": "A photograph 4 inches by 6 inches is enlarged with a scale factor of 2.5. What are the new dimensions? What is the ratio of the areas (original to enlarged)?", "answer": "New dimensions: 10 by 15 inches. Area ratio = 1 : (2.5)² = 1 : 6.25", "hint": ""},
            {"stem": "Two similar triangles have side lengths in ratio 2:5. If the smaller triangle has area 16 cm², what is the area of the larger triangle?", "answer": "Area scales by (scale factor)². Scale factor = 5/2 = 2.5, so area multiplies by 2.5² = 6.25. Larger area = 16 × 6.25 = 100 cm²", "hint": ""},
            {"stem": "A building casts a shadow 50 feet long. At the same time, a 6-foot tall person casts a 4-foot shadow. How tall is the building? Explain why similar triangles work here.", "answer": "The sun's angle creates similar triangles. Height/Shadow = 6/4 = 1.5. Building height = 50 × 1.5 = 75 feet. Similar triangles because same angle of sun elevation.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Prove that if two triangles are similar, their perimeters are in the same ratio as their corresponding sides, but their areas are in the ratio of the square of that number. Use algebra and a specific example.", "answer": "Proof: If sides are in ratio k, then all sides scale by k. Perimeter = sum of sides, so perimeter scales by k. Area involves length × width, so both scale by k, giving k². Example: 3-4-5 triangle vs 6-8-10: side ratio 2:1, perimeter ratio 12:24 = 1:2, area ratio 6:24 = 1:4 = (2)².", "hint": ""},
            {"stem": "A photographer wants to enlarge a 2×3 photo to fit a frame that is 10×15 inches. Can she enlarge it without distortion? Why or why not? What are her options?", "answer": "2:3 ratio = 2/3 ≈ 0.67. 10:15 ratio = 10/15 = 2/3. Yes, same ratio, no distortion! Scale factor = 5. She could also crop to fit any width or add white space.", "hint": ""},
            {"stem": "Create an original word problem involving similar figures that requires at least two steps and has a real-world context. Solve it completely, identifying which property of similar figures you used.", "answer": "Open-ended. Example: 'A tree is 20 feet tall and casts a 12-foot shadow. A garden wants to build a proportional statue that casts a 3-foot shadow. How tall should it be?' Solution: 20/12 = h/3 → h = 5 feet. Uses correspondence of sides in similar figures.", "hint": ""},
        ],
    },
    "transformations": {
        "beginning": [
            {"stem": "A point is at (2, 3). After a translation 4 units right and 2 units up, where is it?", "answer": "(2+4, 3+2) = (6, 5)", "hint": "Add to x for right, add to y for up"},
            {"stem": "What does a reflection across the y-axis do to the coordinates of a point?", "answer": "It changes (x, y) to (-x, y) — the x-coordinate is negated", "hint": "The y-axis is vertical; reflection flips left-right"},
            {"stem": "A square has vertices at (0,0), (1,0), (1,1), (0,1). If rotated 90° clockwise about the origin, where does (1,0) move to?", "answer": "(1,0) moves to (0, -1)", "hint": "Clockwise 90° rotation: (x,y) → (y, -x)"},
        ],
        "partial": [
            {"stem": "Graph triangle with vertices (1,1), (3,1), (2,3). Translate it 2 units left and 1 unit down. List the new vertices.", "answer": "(1-2, 1-1) = (-1, 0); (3-2, 1-1) = (1, 0); (2-2, 3-1) = (0, 2)", "hint": "Subtract for left and down translations"},
            {"stem": "A point (3, 2) is reflected across the x-axis, then translated 1 unit right. Where does it end up?", "answer": "After reflection: (3, -2). After translation: (4, -2)", "hint": "Reflection across x-axis: (x,y) → (x, -y)"},
            {"stem": "Describe the transformation that moves (4,5) to (5, -4). Is it a rotation? If so, about what point and by how much?", "answer": "90° counterclockwise rotation about the origin. Check: (4,5) → (-5, 4)? No. Actually: (x,y) → (y,-x) gives (4,5) → (5,-4) ✓. This is 90° clockwise.", "hint": ""},
        ],
        "proficient": [
            {"stem": "A rectangle with vertices A(0,0), B(4,0), C(4,2), D(0,2) is reflected across the line y = x. Find the new vertices and graph both.", "answer": "Reflection across y=x swaps coordinates: A(0,0)→(0,0), B(4,0)→(0,4), C(4,2)→(2,4), D(0,2)→(2,0). New rectangle is vertical.", "hint": ""},
            {"stem": "Triangle PQR has vertices P(1,2), Q(4,2), R(3,5). Rotate it 180° about the origin. List new vertices. What is the relationship between PQR and P'Q'R'?", "answer": "180° rotation: (x,y) → (-x,-y). P'(-1,-2), Q'(-4,-2), R'(-3,-5). P'Q'R' is congruent (same size/shape) but opposite orientation.", "hint": ""},
            {"stem": "A point starts at (2,3). After a series of transformations, it ends at (-3,-2). One transformation was a 90° counterclockwise rotation about the origin. What other transformation(s) occurred?", "answer": "90° CCW: (2,3) → (-3,2). To get to (-3,-2), need translation 4 units down. Or: reflection across x-axis after rotation. Multiple valid answers.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Describe a sequence of transformations (at least 2) that would map quadrilateral ABCD to A''B''C''D''. Give coordinates for all points. Then create the reverse sequence to map back.", "answer": "Open-ended. Example: Square ABCD at (0,0), (1,0), (1,1), (0,1). Translate 3 right: vertices shift. Reflect across y-axis: negate x-coords. Reverse: reflect across y-axis, then translate 3 left.", "hint": ""},
            {"stem": "Prove that a 180° rotation about a point gives the same result as two consecutive reflections across perpendicular lines through that point. Illustrate with coordinates.", "answer": "Reflect across y-axis: (x,y) → (-x,y). Then reflect across x-axis: (-x,y) → (-x,-y). This equals 180° rotation! Shows rotation is composition of reflections.", "hint": ""},
            {"stem": "Design a floor tile pattern using at least three different transformations (translation, reflection, rotation). Describe the transformations mathematically and explain why your pattern is aesthetically balanced.", "answer": "Open-ended. Example: Start with a triangle. Rotate 90° four times around a center point, then translate the resulting pattern. Creates kaleidoscope effect through rotational symmetry plus translation.", "hint": ""},
        ],
    },
    "mean median range": {
        "beginning": [
            {"stem": "Find the mean of: 2, 4, 6, 8, 10", "answer": "(2+4+6+8+10) ÷ 5 = 30 ÷ 5 = 6", "hint": "Mean = sum of all values ÷ number of values"},
            {"stem": "Find the median of: 1, 3, 5, 7, 9", "answer": "5 (the middle value)", "hint": "Median is the middle value when ordered"},
            {"stem": "Find the range of: 15, 8, 23, 12, 30", "answer": "30 - 8 = 22", "hint": "Range = largest value - smallest value"},
        ],
        "partial": [
            {"stem": "A soccer team scored: 2, 5, 3, 5, 4, 3, 5 goals over seven games. Find the mean, median, and mode.", "answer": "Mean = (2+5+3+5+4+3+5) ÷ 7 = 27 ÷ 7 ≈ 3.86. Median: ordered as 2,3,3,4,5,5,5 → middle is 4. Mode: 5 (appears 3 times)", "hint": "For median with 7 values, the 4th value is in the middle"},
            {"stem": "Test scores: 78, 85, 92, 78, 88, 95. Find mean, median, and range.", "answer": "Mean = 516 ÷ 6 = 86. Median: ordered 78,78,85,88,92,95 → (85+88)÷2 = 86.5. Range = 95-78 = 17", "hint": "With even number of values, median is average of two middle values"},
            {"stem": "A restaurant's daily sales: $1200, $1500, $1400, $900, $1300. Which measure best describes a typical day? Why?", "answer": "Mean = $1260, Median = $1300. Median is better because it's not affected by the low day ($900). Mean slightly lower due to that outlier.", "hint": "Outliers affect mean more than median"},
        ],
        "proficient": [
            {"stem": "Heights of 5 students: 60, 62, 65, 68, 72 inches. If one more student (height 70 in) joins, how does each measure change?", "answer": "Original: mean=65.4, median=65, range=12. New: mean=65.67, median=66, range=12. Mean increased slightly, median increased more, range unchanged.", "hint": ""},
            {"stem": "A data set has 8 values with mean 50. If you add a 9th value of 90, what is the new mean?", "answer": "Sum of 8 values = 8 × 50 = 400. New sum = 400 + 90 = 490. New mean = 490 ÷ 9 ≈ 54.44", "hint": ""},
            {"stem": "Compare: Dataset A: 10, 20, 30, 40, 50. Dataset B: 28, 29, 30, 31, 32. Same mean (30), different ranges and distributions. What does this tell you about using only the mean?", "answer": "A has range 40, B has range 4. Both have mean 30 but very different spreads. Mean alone doesn't show variability — need range or other measures.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "A company reports average salary of $60,000. But half the employees earn $35,000 and half earn $85,000. Explain why the mean is misleading. What would be a better measure to report? Would median, mode, or range help? Explain the ethical dimension.", "answer": "Mean $60k is a value no one actually earns! Bimodal distribution with no middle. Median = $60k (same, misleading here too). Better to show: 50% earn $35k, 50% earn $85k. Or use range ($50k) and modes. Shows importance of transparency over single numbers.", "hint": ""},
            {"stem": "Design a dataset of 10 values where the mean, median, and mode are all different. Then add one outlier (extreme value). How does each measure change? Which changed the most? Explain why.", "answer": "Open-ended. Example: 1,2,2,3,4,5,6,7,8,9. Mean=4.7, Median=4.5, Mode=2. Add 100: new mean≈14.4 (huge change), median=5.5 (small change), mode=2 (unchanged). Mean most affected by outliers.", "hint": ""},
            {"stem": "A teacher notices her class mean test score is 75, but wants to understand why some students score 95 while others score 50. What additional statistical measures should she calculate? Create a complete statistical summary that would help her understand the distribution and write a brief interpretation.", "answer": "Calculate: median, mode, range, quartiles, standard deviation. Then create histogram/box plot. Analysis: large range (45 points) and low median suggest some students struggling. Quartiles show where gaps are. Leads to intervention strategies.", "hint": ""},
        ],
    },
    "probability": {
        "beginning": [
            {"stem": "A coin is flipped. What is the probability of getting heads?", "answer": "P(heads) = 1/2 or 0.5 or 50%", "hint": "Probability = (favorable outcomes) ÷ (total possible outcomes)"},
            {"stem": "A die (1-6) is rolled. What is the probability of rolling a 3?", "answer": "P(3) = 1/6 ≈ 0.167 or about 17%", "hint": "A standard die has 6 equally likely outcomes"},
            {"stem": "A spinner has 4 equal sections: red, blue, green, yellow. What is P(blue)?", "answer": "P(blue) = 1/4 = 0.25 = 25%", "hint": "Each section is equally likely"},
        ],
        "partial": [
            {"stem": "A bag has 5 red marbles, 3 blue, and 2 green. If you draw one marble, what is P(red)?", "answer": "Total = 10. P(red) = 5/10 = 1/2 = 0.5", "hint": "P = (number of red) ÷ (total marbles)"},
            {"stem": "You flip a coin twice. What is the probability of getting two heads?", "answer": "P(HH) = 1/2 × 1/2 = 1/4", "hint": "Use multiplication for independent events"},
            {"stem": "Roll a die twice. What is P(getting a 2 on first roll AND a 4 on second)?", "answer": "P(2 then 4) = (1/6) × (1/6) = 1/36", "hint": "Each roll is independent — multiply probabilities"},
        ],
        "proficient": [
            {"stem": "Survey 100 people about ice cream flavor: vanilla (45), chocolate (30), strawberry (25). Based on this data, estimate P(next person chooses vanilla).", "answer": "P(vanilla) ≈ 45/100 = 0.45 = 45% (experimental probability)", "hint": ""},
            {"stem": "A school raffle sells 500 tickets. You buy 5 tickets. What is the probability you win (assuming 1 winning ticket)?", "answer": "P(win) = 5/500 = 1/100 = 0.01 = 1%", "hint": ""},
            {"stem": "Two cards are drawn from a standard 52-card deck without replacement. What is P(first is a heart AND second is also a heart)?", "answer": "P = (13/52) × (12/51) = 156/2652 ≈ 0.0588 or about 5.9%", "hint": "Second draw has 51 cards remaining, 12 hearts left"},
        ],
        "exemplary": [
            {"stem": "Design an experiment to determine whether a coin is fair (unbiased). How many flips would you do? What would convince you it's unfair? Use probability to justify your threshold.", "answer": "Flip 100+ times. Fair coin: expect ~50 heads. If get 30-70, likely fair (within normal variation). If get <25 or >75, suspicious. Use binomial probability to calculate confidence intervals around 50.", "hint": ""},
            {"stem": "A game: pay $5 to roll a die. If you roll a 6, you win $20. Otherwise, you lose your $5. Is this game fair? Calculate expected value. Create a modified game that is fair.", "answer": "EV = P(win)($15) + P(lose)(-$5) = (1/6)(15) + (5/6)(-5) = 2.5 - 4.17 = -$1.67 (you lose). Fair game: win $30 on roll 6 → EV = (1/6)(25) + (5/6)(-5) = $0.", "hint": ""},
            {"stem": "Research: Birthday paradox — in a group of 23 people, there's >50% chance two share a birthday. Explain why this is counterintuitive. Calculate P(no shared birthdays) and use it to find P(at least one match).", "answer": "Intuition: 23/365 ≈ 6% chance, so seems unlikely. Reality: consider all pairs (23 choose 2 = 253 pairs!). P(all different) = 365/365 × 364/365 × ... = 0.493. P(match) = 1 - 0.493 = 50.7%. Shows why pairwise comparisons matter.", "hint": ""},
        ],
    },
    "linear functions": {
        "beginning": [
            {"stem": "A car travels at 60 mph. Write an equation for distance d traveled in time t hours.", "answer": "d = 60t", "hint": "Distance = rate × time"},
            {"stem": "Graph y = 2x. Is this a linear function?", "answer": "Yes. It's a straight line passing through the origin with slope 2.", "hint": "Linear functions graph as straight lines"},
            {"stem": "For y = 3x + 1, what is the y-intercept?", "answer": "The y-intercept is 1 (where the line crosses the y-axis)", "hint": "y-intercept is the b value in y = mx + b"},
        ],
        "partial": [
            {"stem": "A phone plan costs $30 plus $0.05 per text. Write a linear equation for total cost C and number of texts t.", "answer": "C = 30 + 0.05t (or C = 0.05t + 30)", "hint": "Cost = fixed fee + (rate per text × number of texts)"},
            {"stem": "Find the slope of the line through points (1, 3) and (4, 9).", "answer": "slope = (9-3) ÷ (4-1) = 6 ÷ 3 = 2", "hint": "slope = (y₂ - y₁) ÷ (x₂ - x₁)"},
            {"stem": "A line has slope -2 and passes through (3, 5). Find its y-intercept using y = mx + b.", "answer": "5 = (-2)(3) + b → 5 = -6 + b → b = 11. Equation: y = -2x + 11", "hint": "Substitute the point and slope into y = mx + b"},
        ],
        "proficient": [
            {"stem": "Write the equation of a line parallel to y = 3x - 4 that passes through (2, 5).", "answer": "Parallel lines have same slope (3). Using (2,5): 5 = 3(2) + b → b = -1. Equation: y = 3x - 1", "hint": ""},
            {"stem": "A company's revenue increases by $200 per day, starting from $500 on day 0. Write an equation and find revenue on day 30.", "answer": "R = 500 + 200d. On day 30: R = 500 + 200(30) = $6,500", "hint": ""},
            {"stem": "Graph y = -0.5x + 3. Identify slope, y-intercept, and x-intercept. Verify your x-intercept by substituting.", "answer": "Slope: -0.5. y-intercept: 3. For x-intercept, set y=0: 0 = -0.5x + 3 → x = 6. Verify: y = -0.5(6) + 3 = 0 ✓", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Two companies offer gym memberships: Company A charges $50 initial fee + $20/month. Company B charges $80/month with no initial fee. Write equations for both. When is Company A cheaper? Graph both lines and label the intersection point.", "answer": "A: C = 50 + 20m. B: C = 80m. Equal: 50 + 20m = 80m → 50 = 60m → m = 5/6 month. A cheaper after: 50 + 20m < 80m → 50 < 60m → m > 5/6. Intersection: (5/6, 400/3).", "hint": ""},
            {"stem": "Explain what the slope and y-intercept represent in a real-world context (e.g., savings account, plant growth, temperature). Give two different examples with different interpretations.", "answer": "Savings: y = 25x + 100. Slope (25) = monthly deposit, y-intercept (100) = starting balance. Plant: h = 2d + 5. Slope (2) = growth rate per day, y-intercept (5) = initial height. Same equation structure, different meanings.", "hint": ""},
            {"stem": "Create a multi-step problem that requires writing two linear equations, finding their intersection, and interpreting the solution in context. Then solve it completely.", "answer": "Open-ended. Example: 'Car A starts 50 miles ahead, traveling 50 mph. Car B starts behind, traveling 70 mph. When does B catch up?' A: d = 50 + 50t. B: d = 70t. Equal: 50 + 50t = 70t → t = 2.5 hrs. B catches up at 175 miles.", "hint": ""},
        ],
    },
    "slope intercept": {
        "beginning": [
            {"stem": "In y = mx + b, what does m represent?", "answer": "m is the slope (steepness of the line)", "hint": "Slope = rise/run"},
            {"stem": "In y = 2x + 3, identify m and b.", "answer": "m = 2 (slope), b = 3 (y-intercept)", "hint": "y = mx + b format"},
            {"stem": "What does the y-intercept represent on a graph?", "answer": "The point where the line crosses the y-axis (when x = 0)", "hint": "Set x = 0 to find the y-intercept"},
        ],
        "partial": [
            {"stem": "A line has slope 4 and y-intercept -2. Write the equation in slope-intercept form.", "answer": "y = 4x - 2", "hint": "Just plug m and b into y = mx + b"},
            {"stem": "For y = -3x + 5, describe what happens as x increases by 1.", "answer": "y decreases by 3 (slope is -3, so the line goes down)", "hint": "Slope tells you the change in y for each change in x"},
            {"stem": "Write the equation of a line through (0, 6) with slope 2.", "answer": "Since (0,6) is the y-intercept: y = 2x + 6", "hint": "When you know the y-intercept and slope, just use y = mx + b"},
        ],
        "proficient": [
            {"stem": "Find the equation of the line through (2, 7) and (5, 13) in slope-intercept form.", "answer": "Slope = (13-7)/(5-2) = 6/3 = 2. Using (2,7): 7 = 2(2) + b → b = 3. Equation: y = 2x + 3", "hint": ""},
            {"stem": "Rewrite 3x - 2y = 8 in slope-intercept form. What are the slope and y-intercept?", "answer": "-2y = -3x + 8 → y = 1.5x - 4. Slope = 1.5, y-intercept = -4", "hint": ""},
            {"stem": "A line has slope -1/2 and passes through (4, 1). Write the equation and verify your y-intercept by substituting a different point.", "answer": "1 = (-1/2)(4) + b → 1 = -2 + b → b = 3. Equation: y = -1/2x + 3. Verify with x=0: y=3 ✓", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Interpret the slope and y-intercept for a real business model: Revenue = $500 + $50 per item sold. Write in y = mx + b form. What does each number mean practically? If the company sells 100 items, what is the revenue?", "answer": "y = 50x + 500. Slope (50) = revenue per item. y-intercept (500) = fixed revenue (base earnings). At x=100: y = 50(100) + 500 = $5,500 total revenue.", "hint": ""},
            {"stem": "Compare slopes of y = 2x, y = 5x, y = 0.5x, y = -2x. How does the slope value affect the steepness and direction? Create a sketch showing all four lines.", "answer": "Positive slopes go up right; negative slopes go down right. Larger slope = steeper. |5| > |2| > |0.5|, so y=5x steepest, y=0.5x flattest. y=-2x negative slope is steep downward.", "hint": ""},
            {"stem": "A fitness trainer charges $30 per session plus a $50 annual membership fee. Write the equation where y = total annual cost and x = number of sessions. Explain each component. Then determine break-even: when is the annual cost more than $500?", "answer": "y = 30x + 50. At $500: 30x + 50 = 500 → x = 15 sessions. After 15 sessions, cost exceeds $500. Slope (30) = per-session cost, intercept (50) = fixed membership.", "hint": ""},
        ],
    },
    "systems of equations": {
        "beginning": [
            {"stem": "A system has two equations. To have a solution, what must the lines do?", "answer": "The lines must intersect (cross) at one point", "hint": "The solution is where both equations are true"},
            {"stem": "Solve by inspection: y = 2x and y = x + 3. When does 2x = x + 3?", "answer": "x = 3, so y = 6. Solution: (3, 6)", "hint": "Set the equations equal to each other"},
            {"stem": "Check if (2, 5) is a solution to: y = 2x + 1 and y = x + 3", "answer": "Equation 1: 5 = 2(2) + 1 = 5 ✓. Equation 2: 5 = 2 + 3 = 5 ✓. Yes, (2,5) is the solution.", "hint": "Substitute the point into both equations"},
        ],
        "partial": [
            {"stem": "Solve the system: y = 3x - 1 and y = 2x + 2", "answer": "3x - 1 = 2x + 2 → x = 3. y = 3(3) - 1 = 8. Solution: (3, 8)", "hint": "Set the equations equal and solve for x"},
            {"stem": "Solve using substitution: x + y = 10 and y = x + 2", "answer": "Substitute: x + (x+2) = 10 → 2x = 8 → x = 4. y = 6. Solution: (4, 6)", "hint": "Replace y in the first equation with x+2"},
            {"stem": "Solve using elimination: 2x + y = 7 and x - y = 2", "answer": "Add equations: 3x = 9 → x = 3. Substitute: 3 - y = 2 → y = 1. Solution: (3, 1)", "hint": "Add the equations to eliminate y"},
        ],
        "proficient": [
            {"stem": "Solve: 3x + 2y = 12 and x - y = 1. Use any method and verify.", "answer": "From eq 2: x = y + 1. Substitute: 3(y+1) + 2y = 12 → 5y = 9 → y = 1.8, x = 2.8. Verify: 3(2.8)+2(1.8)=12 ✓, 2.8-1.8=1 ✓", "hint": ""},
            {"stem": "Two angles sum to 180°. One angle is 20° more than the other. Write a system of equations and solve for both angles.", "answer": "x + y = 180 and x = y + 20. Substitute: (y+20) + y = 180 → y = 80°, x = 100°", "hint": ""},
            {"stem": "A store sells apples ($1.50 each) and oranges ($2 each). A customer spends $14 on 8 pieces of fruit. How many apples and oranges? Set up and solve the system.", "answer": "a + o = 8 and 1.5a + 2o = 14. From eq 1: a = 8-o. Substitute: 1.5(8-o) + 2o = 14 → o = 4. a = 4. (4 apples, 4 oranges)", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Explain what it means when a system has: (1) exactly one solution, (2) no solution, (3) infinitely many solutions. Give an example equation pair for each case and explain graphically.", "answer": "(1) One solution: lines intersect at one point (different slopes). (2) No solution: parallel lines (same slope, different intercepts). (3) Infinite: same line (identical equations). Example: (1) y=2x, y=x+1, (2) y=2x, y=2x+5, (3) y=2x+3, 2y=4x+6.", "hint": ""},
            {"stem": "A theater sells adult and child tickets. Adults cost $12, children cost $8. They sold 200 tickets and made $2,000. How many of each? Solve the system and explain any constraints (e.g., can't have negative tickets).", "answer": "a + c = 200, 12a + 8c = 2000. From eq 1: c = 200-a. Substitute: 12a + 8(200-a) = 2000 → 4a = 400 → a = 100, c = 100. Constraint: a,c ≥ 0 (non-negative).", "hint": ""},
            {"stem": "Create a word problem involving a system of equations with real-world context (e.g., mixing solutions, comparing plans, route planning). Solve it using at least two different methods and verify the solution makes sense.", "answer": "Open-ended. Example: 'A recipe needs 3 cups flour, 2 cups sugar (total). Flour costs $0.50/cup, sugar $0.80/cup (total cost $1.90). Find amounts.' f + s = 3, 0.5f + 0.8s = 1.9. Solve to get f = 1, s = 2.", "hint": ""},
        ],
    },
    "pythagorean theorem": {
        "beginning": [
            {"stem": "For a right triangle with legs 3 and 4, use a² + b² = c² to find the hypotenuse.", "answer": "3² + 4² = c² → 9 + 16 = 25 → c = 5", "hint": "Legs are the sides that form the right angle"},
            {"stem": "True or False: The Pythagorean theorem applies to all triangles.", "answer": "False. It only applies to right triangles.", "hint": "The right angle is special"},
            {"stem": "A right triangle has legs 5 and 12. What is the hypotenuse?", "answer": "√(5² + 12²) = √(25 + 144) = √169 = 13", "hint": "c = √(a² + b²)"},
        ],
        "partial": [
            {"stem": "A ladder leans against a wall. The ladder is 10 feet long, and the base is 6 feet from the wall. How high does it reach?", "answer": "6² + h² = 10² → 36 + h² = 100 → h² = 64 → h = 8 feet", "hint": "The ladder is the hypotenuse"},
            {"stem": "A right triangle has hypotenuse 13 and one leg 5. Find the other leg.", "answer": "5² + b² = 13² → 25 + b² = 169 → b² = 144 → b = 12", "hint": "Rearrange to solve for the missing leg"},
            {"stem": "Is a triangle with sides 5, 12, 13 a right triangle? How do you know?", "answer": "Yes. Check: 5² + 12² = 25 + 144 = 169 = 13² ✓. It satisfies Pythagorean theorem.", "hint": "If a² + b² = c², it's a right triangle"},
        ],
        "proficient": [
            {"stem": "Two cities are 300 miles north and 400 miles east of your location. What is the straight-line distance between them?", "answer": "This forms a right triangle: √(300² + 400²) = √(90,000 + 160,000) = √250,000 = 500 miles", "hint": ""},
            {"stem": "A right triangle has legs 7 and 24. Verify it's a 7-24-25 Pythagorean triple by checking a² + b² = c².", "answer": "7² + 24² = 49 + 576 = 625 = 25². Yes, verified.", "hint": ""},
            {"stem": "A diagonal of a rectangle is 17 inches, and one side is 8 inches. Find the other dimension.", "answer": "8² + b² = 17² → 64 + b² = 289 → b² = 225 → b = 15 inches", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Prove the Pythagorean theorem geometrically using areas. Show how the square of the hypotenuse equals the sum of squares of the legs.", "answer": "Visual proof: on a right triangle, draw squares on each side. The large square (c²) can be rearranged from the two smaller squares (a² and b²). This shows a² + b² = c² through area conservation.", "hint": ""},
            {"stem": "In a 3D space, a box has dimensions 3, 4, and 5 units. What is the space diagonal (distance from one corner to the opposite corner)? Hint: use Pythagorean theorem twice.", "answer": "First, diagonal of base: √(3² + 4²) = 5. Then, space diagonal: √(5² + 5²) = √50 = 5√2 ≈ 7.07 units. Or directly: √(3² + 4² + 5²) = √50.", "hint": ""},
            {"stem": "Research and explain: Why are Pythagorean triples (like 3-4-5, 5-12-13, 8-15-17) useful in construction and surveying? Create your own Pythagorean triple using a formula and verify it.", "answer": "Triples give whole-number measurements (no decimals). In construction, 3-4-5 ensures right angles. Formula: (2n, n²-1, n²+1) for n>1. Example: n=3 → (6,8,10). Verify: 6²+8²=36+64=100=10² ✓", "hint": ""},
        ],
    },
    "scientific notation": {
        "beginning": [
            {"stem": "Write 2,500 in scientific notation.", "answer": "2.5 × 10³", "hint": "Move decimal to make a number between 1 and 10"},
            {"stem": "Write 0.00045 in scientific notation.", "answer": "4.5 × 10⁻⁴", "hint": "Negative exponent for numbers less than 1"},
            {"stem": "What does 3.2 × 10² equal?", "answer": "3.2 × 100 = 320", "hint": "Multiply 3.2 by 100"},
        ],
        "partial": [
            {"stem": "Convert 1.8 × 10⁶ to standard form.", "answer": "1,800,000", "hint": "10⁶ means move decimal 6 places right"},
            {"stem": "Convert 5.6 × 10⁻³ to standard form.", "answer": "0.0056", "hint": "Negative exponent means move decimal left"},
            {"stem": "Which is larger: 2.1 × 10⁴ or 1.9 × 10⁵?", "answer": "1.9 × 10⁵ = 190,000 is larger than 2.1 × 10⁴ = 21,000", "hint": "Compare the exponents first"},
        ],
        "proficient": [
            {"stem": "Multiply: (2 × 10³) × (3 × 10²). Express in scientific notation.", "answer": "(2 × 3) × (10³ × 10²) = 6 × 10⁵", "hint": ""},
            {"stem": "Divide: (8 × 10⁶) ÷ (2 × 10³). Express in scientific notation.", "answer": "(8 ÷ 2) × (10⁶ ÷ 10³) = 4 × 10³", "hint": ""},
            {"stem": "The sun is 93,000,000 miles away. Write this in scientific notation. The speed of light is 186,000 miles/second. How long does it take light to reach Earth?", "answer": "Distance: 9.3 × 10⁷ miles. Time = distance ÷ speed = (9.3 × 10⁷) ÷ (1.86 × 10⁵) ≈ 500 seconds ≈ 8.3 minutes", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Compare the size of Earth and Sun: Earth diameter ≈ 8 × 10⁶ m, Sun diameter ≈ 1.4 × 10⁹ m. How many times wider is the Sun? Explain why scientific notation is essential for this comparison.", "answer": "(1.4 × 10⁹) ÷ (8 × 10⁶) = (1.4 ÷ 8) × 10³ ≈ 0.175 × 10³ = 175 times. Scientific notation makes huge numbers manageable and comparisons clear. Without it: 1,400,000,000 ÷ 8,000,000 is harder to compute mentally.", "hint": ""},
            {"stem": "The national debt is about $33 trillion. Express this in scientific notation. If every US resident (330 million) paid an equal share, how much would each person owe? Use scientific notation throughout.", "answer": "Debt: 3.3 × 10¹³ dollars. Population: 3.3 × 10⁸. Per capita: (3.3 × 10¹³) ÷ (3.3 × 10⁸) = 10⁵ = $100,000 per person.", "hint": ""},
            {"stem": "Create a research problem involving extremely large or small numbers (atoms, stars, microbes, distances). Convert to scientific notation and perform calculations. Explain why scientific notation was necessary.", "answer": "Open-ended. Example: 'Number of bacteria in a petri dish doubles every hour. Start with 5 × 10³ bacteria. After 24 hours: 5 × 10³ × 2²⁴ ≈ 8 × 10¹⁰ bacteria.' Shows exponential growth with scientific notation.", "hint": ""},
        ],
    },
    "irrational numbers": {
        "beginning": [
            {"stem": "Which numbers are irrational?\n(a) 1/2  (b) √2  (c) 3.14  (d) π", "answer": "(b) √2 and (d) π are irrational", "hint": "Irrational numbers cannot be written as fractions and decimals don't repeat"},
            {"stem": "Is √9 rational or irrational? Why?", "answer": "Rational, because √9 = 3, which is an integer.", "hint": "If a square root is a whole number, it's rational"},
            {"stem": "Approximate √10 to the nearest tenth.", "answer": "√10 ≈ 3.2 (since 3.2² = 10.24)", "hint": "Find two perfect squares it's between: 9 and 16"},
        ],
        "partial": [
            {"stem": "Is √16/√4 rational or irrational? Simplify.", "answer": "√16/√4 = 4/2 = 2, which is rational.", "hint": "Simplify each square root, then divide"},
            {"stem": "Which is larger: √5 or 2.2? Estimate √5.", "answer": "√5 ≈ 2.236, which is slightly larger than 2.2", "hint": "Since 2.236² ≈ 5 and 2.2² = 4.84"},
            {"stem": "Order from least to greatest: 3, √10, π, 22/7", "answer": "3, √10 ≈ 3.16, π ≈ 3.14... wait: 3 < π < √10 < 22/7 ≈ 3.14. Actually: 3 < π ≈ 3.14 < 22/7 ≈ 3.14 < √10 ≈ 3.16", "hint": "Approximate each value"},
        ],
        "proficient": [
            {"stem": "Simplify √50. Is it rational or irrational?", "answer": "√50 = √(25 × 2) = 5√2. This is irrational because √2 is irrational.", "hint": ""},
            {"stem": "Plot √2, √3, √4, √5 on a number line. Which are rational? Which are irrational?", "answer": "√2 ≈ 1.41 (irrational), √3 ≈ 1.73 (irrational), √4 = 2 (rational), √5 ≈ 2.24 (irrational). Only √4 is rational.", "hint": ""},
            {"stem": "A square has area 18 square units. What is the side length? Is it rational or irrational?", "answer": "Side = √18 = 3√2 ≈ 4.24 units. This is irrational.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Prove that √2 is irrational. Use a proof by contradiction.", "answer": "Assume √2 is rational: √2 = a/b in lowest terms. Then 2 = a²/b² → 2b² = a². So a² is even → a is even → a = 2k. Then 2b² = 4k² → b² = 2k² → b is even. Both even contradicts 'lowest terms.' Therefore √2 is irrational.", "hint": ""},
            {"stem": "Explain how irrational numbers fit on the number line even though you can't write them exactly. Use √2 as an example with decimal approximations.", "answer": "√2 lies between 1 and 2 (since 1² < 2 < 2²). More precisely: 1.4² = 1.96, 1.5² = 2.25, so 1.4 < √2 < 1.5. Each decade, we can find tighter bounds. Even though decimal is infinite non-repeating, its position on the line is well-defined.", "hint": ""},
            {"stem": "Classify these numbers as rational or irrational and explain: √4, ∛8, π, √(9/16), e (Euler's number), 0.123123123...", "answer": "Rational: √4=2, ∛8=2, √(9/16)=3/4, 0.123... (repeating). Irrational: π, e. Key: if it's repeating decimal or can be written a/b, it's rational. Non-repeating decimals and special constants are irrational.", "hint": ""},
        ],
    },
    "scatterplot": {
        "beginning": [
            {"stem": "What does a scatter plot show?", "answer": "The relationship between two variables (one on each axis)", "hint": "Each point represents a data pair (x, y)"},
            {"stem": "If points on a scatter plot trend upward from left to right, what does this show?", "answer": "A positive correlation — as one variable increases, the other tends to increase", "hint": "Upward trend = positive, downward = negative"},
            {"stem": "Plot points: (1,2), (2,4), (3,6). Describe the relationship.", "answer": "Perfect positive linear relationship: y = 2x", "hint": "The points form a straight line"},
        ],
        "partial": [
            {"stem": "Scatter plot shows student study hours (x) vs test scores (y). What would a strong positive correlation look like? Weak negative?", "answer": "Strong positive: points closely follow an upward line. Weak negative: points scatter, slight downward trend.", "hint": "Correlation strength depends on how tightly points cluster around a line"},
            {"stem": "Data: (1,8), (2,7), (3,6), (4,5), (5,4). Plot these and describe the correlation.", "answer": "Perfect negative linear relationship: y = -x + 9. Strong negative correlation.", "hint": "Check if points form a line with negative slope"},
            {"stem": "Use a line of best fit through the scatter plot of point (0,0), (1,2), (2,3), (3,5). Estimate y when x = 4.", "answer": "Line approximately y ≈ 1.6x. At x=4: y ≈ 6.4", "hint": "Find a line that minimizes distance to all points"},
        ],
        "proficient": [
            {"stem": "A scatter plot shows temperature (°F) vs ice cream sales. Estimate the correlation coefficient (positive, negative, or none). What does this tell you?", "answer": "Strong positive correlation expected. Higher temps → higher sales. Doesn't prove causation, but shows association.", "hint": ""},
            {"stem": "Calculate the line of best fit for: (1,3), (2,5), (3,7). Compare with actual data. Where does the line underestimate?", "answer": "Line: y = 2x + 1. Check points: (1,3) actual vs 3 fitted—perfect; (2,5) actual vs 5 fitted—perfect; (3,7) actual vs 7 fitted—perfect. This line fits perfectly.", "hint": ""},
            {"stem": "A scatter plot of height vs arm span shows positive correlation. Can you use it to predict arm span from height? What are limitations?", "answer": "Yes, with caution. Line of best fit gives estimates. Limitations: individuals vary, trend doesn't guarantee accuracy for outliers, correlation ≠ causation.", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Collect or create data showing: (1) strong positive correlation, (2) strong negative correlation, (3) no correlation. Plot all three and explain what each reveals about the relationship.", "answer": "Example data: (1) Hours studied vs test score (positive), (2) Car age vs resale value (negative), (3) Shoe size vs favorite color (no correlation). Explains causation vs association.", "hint": ""},
            {"stem": "Two variables show a strong correlation. Explain three ways this correlation could exist: (1) one causes the other, (2) both caused by a third variable, (3) coincidence. Give examples.", "answer": "(1) Causation: more study → higher test scores. (2) Confounding: ice cream sales & drownings both peak in summer (heat causes both). (3) Coincidence: Nicolas Cage films released per year & swimming pool drownings (spurious correlation).", "hint": ""},
            {"stem": "Create a real-world research question involving two variables. Predict the correlation, design a data collection plan, and explain how you would create the scatter plot and line of best fit to test your prediction.", "answer": "Open-ended. Example: 'Does class size correlate with student grades?' Predict: negative (smaller classes, better grades). Collect data from multiple schools. Plot classes on x, avg grade on y. Fit line and assess correlation strength.", "hint": ""},
        ],
    },
    "exponents": {
        "beginning": [
            {"stem": "Evaluate: 2⁵", "answer": "2⁵ = 2 × 2 × 2 × 2 × 2 = 32", "hint": "Multiply the base by itself 5 times"},
            {"stem": "What does 3⁰ equal?", "answer": "3⁰ = 1 (any number to the power 0 equals 1)", "hint": "This is a special rule"},
            {"stem": "Evaluate: 10³", "answer": "10³ = 1,000", "hint": "For powers of 10, count the zeros"},
        ],
        "partial": [
            {"stem": "Simplify: 2³ × 2²", "answer": "2³ × 2² = 2^(3+2) = 2⁵ = 32", "hint": "When multiplying powers with same base, add exponents"},
            {"stem": "Simplify: 5⁴ ÷ 5²", "answer": "5⁴ ÷ 5² = 5^(4-2) = 5² = 25", "hint": "When dividing powers with same base, subtract exponents"},
            {"stem": "Evaluate: (3²)³", "answer": "(3²)³ = 3^(2×3) = 3⁶ = 729", "hint": "Multiply exponents when raising a power to a power"},
        ],
        "proficient": [
            {"stem": "Simplify: (2 × 3)² and compare with 2² × 3². Are they equal?", "answer": "(2 × 3)² = 6² = 36. 2² × 3² = 4 × 9 = 36. Yes, equal. (ab)ⁿ = aⁿ × bⁿ", "hint": ""},
            {"stem": "Evaluate: 2⁻³", "answer": "2⁻³ = 1/(2³) = 1/8", "hint": "Negative exponents mean divide (or take reciprocal)"},
            {"stem": "Simplify: (x²y³)⁴", "answer": "(x²y³)⁴ = x⁸y¹² (multiply exponents)", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Explain why bⁿ × bᵐ = b^(n+m) using the definition of exponents (repeated multiplication).", "answer": "b ⁿ means b multiplied n times. bᵐ means b multiplied m times. Together: b × b × ... (n times) × b × b × ... (m times) = b × b × ... (n+m times) = b^(n+m).", "hint": ""},
            {"stem": "Evaluate without a calculator: (1/2)⁻² × 4³ ÷ 2². Show all steps and explain the properties you used.", "answer": "(1/2)⁻² = 2² = 4. Then 4 × 4³ ÷ 2² = 4⁴ ÷ 4 = 4³ = 64. Used: negative exponent rule, properties of exponents.", "hint": ""},
            {"stem": "Bacteria grow exponentially: N = 100 × 2^t where t is time in hours. How many bacteria after 5 hours? If you start with 50 bacteria instead, write the new formula. Explain what 2 represents (the growth factor).", "answer": "After 5 hrs: N = 100 × 2⁵ = 3,200 bacteria. New formula: N = 50 × 2^t. The 2 (growth factor) means population doubles each hour. Shows exponential vs linear growth.", "hint": ""},
        ],
    },
    "arithmetic sequence": {
        "beginning": [
            {"stem": "What is the common difference in this sequence: 3, 7, 11, 15, 19?", "answer": "Common difference = 4 (each term is 4 more than the previous)", "hint": "Subtract any two consecutive terms"},
            {"stem": "Find the next three terms: 2, 5, 8, 11, ...?", "answer": "14, 17, 20 (add 3 each time)", "hint": "Common difference = 3"},
            {"stem": "Is this an arithmetic sequence? 1, 2, 4, 8, 16", "answer": "No — the differences are 1, 2, 4, 8 (not constant). This is geometric.", "hint": "Arithmetic requires constant difference"},
        ],
        "partial": [
            {"stem": "The first term is 5 and common difference is 3. Write the first 5 terms.", "answer": "5, 8, 11, 14, 17", "hint": "Add d to each previous term"},
            {"stem": "Find the 10th term of: 2, 6, 10, 14, ....", "answer": "First term a₁ = 2, d = 4. a₁₀ = 2 + (10-1)×4 = 2 + 36 = 38", "hint": "Use formula aₙ = a₁ + (n-1)d"},
            {"stem": "A theater seat pricing: Row 1 costs $20, Row 2 costs $22, Row 3 costs $24. How much does Row 15 cost?", "answer": "a₁ = 20, d = 2, n = 15. a₁₅ = 20 + (15-1)×2 = 20 + 28 = $48", "hint": ""},
        ],
        "proficient": [
            {"stem": "Write the equation for the nth term: 5, 12, 19, 26, .... Find the 20th term.", "answer": "d = 7, a₁ = 5. aₙ = 5 + (n-1)×7 = 7n - 2. a₂₀ = 7(20) - 2 = 138", "hint": ""},
            {"stem": "Sum the first 10 terms of: 3, 7, 11, 15, ....", "answer": "a₁ = 3, a₁₀ = 3 + 9×4 = 39. Sum = (10/2)(3 + 39) = 5 × 42 = 210", "hint": "Use Sₙ = (n/2)(a₁ + aₙ)"},
            {"stem": "A savings plan: save $10 first week, $15 second week, $20 third week, etc. How much saved in week 12? Total saved after 12 weeks?", "answer": "a₁₂ = 10 + 11×5 = 65 dollars. S₁₂ = (12/2)(10 + 65) = 6 × 75 = $450", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Prove that an arithmetic sequence with first term a and common difference d has nth term aₙ = a + (n-1)d. Show why this formula works.", "answer": "a₁ = a. a₂ = a + d. a₃ = a + 2d. Pattern: aₙ = a + (n-1)d because we add d exactly (n-1) times to the first term.", "hint": ""},
            {"stem": "Compare arithmetic sequence (constant difference) with geometric sequence (constant ratio). Create an example of each with 5 terms. Calculate the 10th term and sum of first 10 terms for each. Explain which grows faster.", "answer": "Arithmetic: 2, 5, 8, 11, 14. a₁₀ = 29, S₁₀ = 155. Geometric: 2, 6, 18, 54, 162. a₁₀ = 39,366, S₁₀ = 59,048. Geometric grows much faster due to multiplicative vs additive growth.", "hint": ""},
            {"stem": "Create a real-world context where an arithmetic sequence makes sense (e.g., training plan, payment schedule, plant growth). Write the sequence, find the general formula, and answer a relevant question.", "answer": "Open-ended. Example: 'Training: run 1 mile day 1, 1.5 miles day 2, 2 miles day 3, etc.' aₙ = 1 + 0.5(n-1) = 0.5n + 0.5. After 30 days: 0.5(30) + 0.5 = 15.5 miles. Total distance: S₃₀ = (30/2)(1 + 15.5) = 247.5 miles.", "hint": ""},
        ],
    },
    "volume surface area": {
        "beginning": [
            {"stem": "What is the volume of a rectangular box with length 3, width 2, height 4?", "answer": "V = length × width × height = 3 × 2 × 4 = 24 cubic units", "hint": "Volume = l × w × h"},
            {"stem": "A cylinder has radius 2 and height 5. Its volume is V = πr²h. Calculate.", "answer": "V = π × 2² × 5 = 20π ≈ 62.8 cubic units", "hint": "Remember r is the radius, not diameter"},
            {"stem": "True or False: Surface area and volume have the same units.", "answer": "False. Volume is cubic (3D), surface area is square (2D).", "hint": "Volume: cubic units, Surface area: square units"},
        ],
        "partial": [
            {"stem": "A cylinder has radius 3 and height 7. Find its surface area: SA = 2πr² + 2πrh.", "answer": "SA = 2π(3²) + 2π(3)(7) = 18π + 42π = 60π ≈ 188.5 square units", "hint": "Two circular ends + lateral surface"},
            {"stem": "A rectangular prism has dimensions 2, 3, and 5. Find surface area and volume.", "answer": "V = 2 × 3 × 5 = 30. SA = 2(2×3) + 2(2×5) + 2(3×5) = 12 + 20 + 30 = 62 square units", "hint": "Surface area has 6 faces (3 pairs of rectangles)"},
            {"stem": "A sphere has radius 4. Its volume is V = (4/3)πr³. Find volume.", "answer": "V = (4/3)π(4³) = (4/3)π(64) = 256π/3 ≈ 268.1 cubic units", "hint": ""},
        ],
        "proficient": [
            {"stem": "A cylinder and sphere have the same radius (r = 5) and the cylinder has height 10. Compare their volumes.", "answer": "Cylinder: V = π(5²)(10) = 250π. Sphere: V = (4/3)π(5³) = 500π/3 ≈ 166.7π. Cylinder larger by factor of 1.5", "hint": ""},
            {"stem": "A container is a cylinder with radius 5 cm and height 20 cm. If it's filled with water, what is the volume? Express in liters (1 liter = 1000 cm³).", "answer": "V = π(5²)(20) = 500π ≈ 1570.8 cm³ ≈ 1.57 liters", "hint": ""},
            {"stem": "A gift box is wrapped with paper covering its surface. The box is 10 × 8 × 6 inches. How much paper is needed (surface area)?", "answer": "SA = 2(10×8) + 2(10×6) + 2(8×6) = 160 + 120 + 96 = 376 square inches", "hint": ""},
        ],
        "exemplary": [
            {"stem": "Design a can (cylinder) that holds 355 mL (355 cm³). What dimensions minimize the surface area (and thus material used)? Calculate the surface area. Compare with standard cans.", "answer": "For fixed volume, optimal cylinder has h = 2r. With V = πr²h = 355: πr²(2r) = 355 → r ≈ 3.8, h ≈ 7.6. SA ≈ 281 cm². Standard 12 oz can: similar dimensions, showing engineers optimize material efficiency.", "hint": ""},
            {"stem": "A composite shape: cylinder on top of a rectangular prism base. Cylinder has radius 2 and height 3. Prism base is 4 × 4 × 5 (height). Calculate total volume and total surface area (accounting for shared face).", "answer": "Prism volume: 4 × 4 × 5 = 80. Cylinder volume: π(2²)(3) = 12π ≈ 37.7. Total ≈ 117.7. Surface area: prism sides (excluding top) + cylinder (excluding bottom where attached) + shared area circle. Calculation shows need for careful attention to touching surfaces.", "hint": ""},
            {"stem": "A sphere and cube have the same volume (100 cubic units). Which has greater surface area? Calculate both and explain the result. What does this reveal about shape efficiency?", "answer": "Cube: side = ∛100 ≈ 4.64, SA ≈ 129.7. Sphere: r = ∛(75/π) ≈ 2.88, SA ≈ 104.1. Cube has larger surface area. Sphere encloses volume most efficiently — important for cells, planets, containers.", "hint": ""},
        ],
    },
}



def generate_leveled_problems(topic_keywords, grade=None, num_per_level=3):
    """
    Generate differentiated problems at 4 proficiency levels for the given topics.

    Args:
        topic_keywords: list of topic strings (e.g., ["area of circle", "circumference"])
        grade: 7 or 8 (used for standards alignment)
        num_per_level: max problems per level (default 3)

    Returns:
        dict with keys: topic, levels (list of 4 dicts, each with label, color, problems, standards)
    """
    import random

    # Find matching topics in the bank with progressive fallback strategy
    matched_topic = None

    # Strategy 1: Try exact match
    for kw in topic_keywords:
        kw_lower = kw.lower().strip()
        if kw_lower in LEVELED_PROBLEM_BANK:
            matched_topic = kw_lower
            break

    # Strategy 2: Try partial match (substring matching)
    if not matched_topic:
        for kw in topic_keywords:
            kw_lower = kw.lower().strip()
            for bank_topic in LEVELED_PROBLEM_BANK:
                if kw_lower in bank_topic or bank_topic in kw_lower:
                    matched_topic = bank_topic
                    break
            if matched_topic:
                break

    # Strategy 3: Try matching against vocabulary in grade-level standards
    if not matched_topic and grade:
        standards_db = GRADE_7 if grade == 7 else GRADE_8
        all_vocab = set()
        for benchmark_data in standards_db.values():
            all_vocab.update(benchmark_data.get("vocabulary", []))

        # Check if any keyword matches vocabulary
        for kw in topic_keywords:
            kw_lower = kw.lower().strip()
            for vocab in all_vocab:
                if kw_lower in vocab.lower() or vocab.lower() in kw_lower:
                    # Find a topic that uses this vocabulary
                    for bank_topic in LEVELED_PROBLEM_BANK:
                        if vocab.lower() in bank_topic.lower():
                            matched_topic = bank_topic
                            break
                if matched_topic:
                    break
            if matched_topic:
                break

    # Strategy 4: Create generic "practice" set from benchmark descriptions
    if not matched_topic:
        # Construct a generic problem bank from standards
        matched_topic = "custom_practice"
        bank = _build_generic_problems_from_standards(topic_keywords, grade)
    else:
        bank = LEVELED_PROBLEM_BANK[matched_topic]

    # Get standards alignment
    alignment = align_lesson(topic_keywords, grade=grade)
    benchmarks = [b["id"] for b in alignment.get("benchmarks", [])]

    levels = []
    for level_key in ["beginning", "partial", "proficient", "exemplary"]:
        level_meta = PROFICIENCY_LEVELS[level_key]
        problems = bank.get(level_key, [])

        # Select up to num_per_level problems
        selected = problems[:num_per_level]

        # Fill templates with values
        filled = []
        for prob in selected:
            filled.append({
                "stem": _fill_template(prob["stem"]),
                "answer": _fill_template(prob["answer"]),
                "hint": prob.get("hint", ""),
            })

        levels.append({
            "key": level_key,
            "label": level_meta["label"],
            "color_hex": level_meta["color_hex"],
            "description": level_meta["description"],
            "scaffolding": level_meta["scaffolding"],
            "complexity": level_meta["complexity"],
            "verb_bank": level_meta["verb_bank"],
            "problems": filled,
        })

    return {
        "topic": matched_topic,
        "levels": levels,
        "benchmarks": benchmarks[:3],
    }


def _build_generic_problems_from_standards(topic_keywords, grade=None):
    """
    Build a generic problem bank from standards when no specific topic matches.
    Uses benchmark descriptions to generate appropriate problems.

    Args:
        topic_keywords: list of keywords to match against standards
        grade: 7 or 8

    Returns:
        dict with structure matching LEVELED_PROBLEM_BANK entries
    """
    standards_db = GRADE_7 if grade == 7 else GRADE_8

    # Find relevant benchmarks
    relevant_benchmarks = []
    for benchmark_id, benchmark_data in standards_db.items():
        desc = benchmark_data.get("description", "").lower()
        for kw in topic_keywords:
            if kw.lower() in desc:
                relevant_benchmarks.append(benchmark_data)
                break

    # Build generic problem bank
    generic_bank = {
        "beginning": [
            {"stem": "Review the standard: Based on the topic, name a key vocabulary term.",
             "answer": "Answers vary; common terms from the standard apply.",
             "hint": "Look at the vocabulary list for the benchmark"},
            {"stem": "Identify: Which of these is an example of the main concept covered in this standard?",
             "answer": "Answers vary by topic; refer to benchmark description.",
             "hint": "The description explains what students should understand"},
            {"stem": "Recall: What is the primary mathematical skill you should be able to demonstrate?",
             "answer": "Answers vary; based on the standard's description.",
             "hint": "The benchmark specifies what students should know and do"},
        ],
        "partial": [
            {"stem": "Explain: How does the concept from this benchmark connect to real-world applications?",
             "answer": "Answers vary; use benchmark description to guide reasoning.",
             "hint": "Think about where this math skill is used outside the classroom"},
            {"stem": "Compare: How is this concept different from related ones at a lower grade level?",
             "answer": "Answers vary; this benchmark represents increased sophistication.",
             "hint": "Grade 7/8 standards build on earlier skills"},
            {"stem": "Apply: Create a scenario where you would use the skills in this benchmark.",
             "answer": "Answers vary; context should match the benchmark's expectations.",
             "hint": "Think of a realistic situation requiring these mathematical skills"},
        ],
        "proficient": [
            {"stem": "Analyze: What are the key steps to solve a problem related to this benchmark? Explain your reasoning.",
             "answer": "Answers vary; should demonstrate understanding of the mathematical process.",
             "hint": ""},
            {"stem": "Construct: Create an original problem that requires demonstrating proficiency in this benchmark's content.",
             "answer": "Answers vary; student-created problems should be mathematically sound.",
             "hint": ""},
            {"stem": "Justify: Explain why the procedure or concept in this benchmark works mathematically.",
             "answer": "Answers vary; justification should cite mathematical properties or rules.",
             "hint": ""},
        ],
        "exemplary": [
            {"stem": "Design: Create a multi-step investigation that explores this benchmark's concept in depth. Include conjectures and verification.",
             "answer": "Open-ended; student work should show deep mathematical thinking and reasoning.",
             "hint": ""},
            {"stem": "Evaluate: Compare multiple approaches to solving a problem based on this benchmark. Which is most efficient and why?",
             "answer": "Open-ended; analysis should evaluate mathematical elegance and efficiency.",
             "hint": ""},
            {"stem": "Create: Design an original problem that integrates this benchmark with concepts from other standards. Solve it and explain the connections.",
             "answer": "Open-ended; response should demonstrate integration and higher-order thinking.",
             "hint": ""},
        ],
    }

    return generic_bank


# ─── AI IMAGE PROMPT GENERATOR ───────────────────────────────

def generate_image_prompts(topic_keywords, story_context="", num_prompts=5):
    """
    Generate AI image generation prompts for lesson visuals.

    Returns a list of dicts: [{slide_type, prompt, style_notes}, ...]

    These prompts are designed for DALL-E, Midjourney, or similar tools.
    """
    prompts = []

    # Story/narrative image
    if story_context:
        prompts.append({
            "slide_type": "STORY_NARRATIVE",
            "prompt": f"A warm, illustrated scene of {story_context}. Modern flat illustration style, soft lighting, diverse characters, educational setting. No text in image.",
            "style_notes": "16:9 aspect ratio, muted tones with one pop color, no clipart feel",
        })

    # Topic-specific visuals
    topic_images = {
        "circumference": {
            "prompt": "A photorealistic overhead view of a bicycle wheel on a workbench, with a measuring tape wrapped around the tire showing the circumference. Clean workshop setting, natural lighting.",
            "slide_type": "PROBLEM_SLIDE",
        },
        "area of circle": {
            "prompt": "Top-down view of a round pizza on a grid cutting board, showing the circle perfectly aligned to the grid squares. Some squares are whole, some partial. Professional food photography style.",
            "slide_type": "ACTIVITY_LAUNCH",
        },
        "pi": {
            "prompt": "An artistic visualization of the number pi: digits 3.14159... spiraling outward from a glowing circle, on a dark background. Mathematical beauty, clean digital art.",
            "slide_type": "STORY_DRAMATIC",
        },
        "diameter": {
            "prompt": "A cross-section view of a tree trunk showing growth rings, with a ruler measuring across the center (diameter). Nature photography, educational feel.",
            "slide_type": "NOTICE_WONDER",
        },
        "radius": {
            "prompt": "An aerial drone photo of a circular fountain in a park, with a person walking from the center to the edge (showing the radius). Birds-eye view, urban park setting.",
            "slide_type": "NOTICE_WONDER",
        },
        "proportional relationships": {
            "prompt": "A split-image comparison: small coffee cup next to large coffee cup, with proportional steam wisps. Clean product photography on white background.",
            "slide_type": "WOULD_YOU_RATHER",
        },
        "scaling": {
            "prompt": "An architect's drafting table with a floor plan blueprint and a ruler, showing scale markings. Warm overhead lighting, professional workspace.",
            "slide_type": "PROBLEM_SLIDE",
        },
        "distance rate time": {
            "prompt": "A modern train speeding along tracks through a countryside landscape, motion blur on scenery but train sharp. Dynamic angle, golden hour lighting.",
            "slide_type": "STORY_NARRATIVE",
        },
        "pythagorean theorem": {
            "prompt": "An overhead photo of a construction site corner where two walls meet at a right angle, with a measuring tape showing the diagonal. Hard hat visible, real-world application.",
            "slide_type": "PROBLEM_SLIDE",
        },
        "linear functions": {
            "prompt": "A ski slope with a straight run from top to bottom, overlaid with a subtle coordinate grid showing the slope as rise/run. Winter sports photography, clean lines.",
            "slide_type": "STORY_NARRATIVE",
        },
        "probability": {
            "prompt": "Close-up of colorful dice mid-roll on a wooden table, frozen in motion. Sharp focus, shallow depth of field, warm lighting.",
            "slide_type": "NOTICE_WONDER",
        },
        "irrational numbers": {
            "prompt": "A spiral galaxy photograph with the golden ratio spiral overlaid subtly. Space photography meets mathematical beauty.",
            "slide_type": "STORY_NARRATIVE",
        },
    }

    for kw in topic_keywords:
        kw_lower = kw.lower()
        if kw_lower in topic_images:
            prompts.append({
                "slide_type": topic_images[kw_lower]["slide_type"],
                "prompt": topic_images[kw_lower]["prompt"],
                "style_notes": "16:9, high resolution, no text overlays",
            })

    # Always include a generic team collaboration image
    prompts.append({
        "slide_type": "GROUP_DISCUSSION",
        "prompt": "Four diverse middle school students working together at a table with notebooks and calculators, actively discussing and pointing at a shared paper. Warm classroom lighting, authentic educational setting. No text.",
        "style_notes": "16:9, natural poses, inclusive representation",
    })

    return prompts[:num_prompts]


# ─── CLI DEMO ──────────────────────────────────────────────────

if __name__ == "__main__":
    # Demo: align lesson 9.1.1 "What is the Multiplier?"
    print(format_standards_report(
        topic_keywords=["circumference", "pi", "diameter", "proportional relationships", "multiplier"],
        lesson_name="9.1.1 What is the Multiplier?",
        grade=7,
    ))
    print()

    # Demo: align lesson 7.1.1 "Distance, Rate, and Time"
    print(format_standards_report(
        topic_keywords=["distance rate time", "proportional relationships", "unit rate", "slope"],
        lesson_name="7.1.1 Distance, Rate, and Time",
        grade=7,
    ))
    print()

    # Demo: vocab prompts
    vocab = get_vocabulary_for_lesson(["circumference", "pi", "diameter"], grade=7)
    print("Vocabulary prompts for circumference lesson:")
    for role, prompt in generate_vocab_discussion_prompts(vocab):
        print(f"  {role}: {prompt}")
