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
