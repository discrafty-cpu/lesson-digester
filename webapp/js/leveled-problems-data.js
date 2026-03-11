// ==================== DOK LEVELED PROBLEMS DATABASE ====================
// Depth of Knowledge leveled practice problems for MCA-III topics
// DOK 1 = Recall, DOK 2 = Skill/Concept, DOK 3 = Strategic Thinking
// Keyed by topic name matching TEACHING_INSIGHTS and TOPIC_PATTERNS
// ======================================================================

const DOK_PROBLEMS = {

    // ======================== GRADE 6 ========================

    'locate and compare numbers': {
        grade: 6,
        dok1: [
            { stem: 'Place 3/4 on a number line from 0 to 1.', answer: 'Between 1/2 and 1, closer to 1', hint: 'Divide the line into 4 equal parts.' },
            { stem: 'Which is greater: 0.6 or 0.58?', answer: '0.6 > 0.58', hint: 'Compare the tenths place first.' },
            { stem: 'Order from least to greatest: 1/2, 0.3, 75%', answer: '0.3, 1/2, 75%', hint: 'Convert all to decimals first.' }
        ],
        dok2: [
            { stem: 'Marcus says 3/8 > 3/4 because 8 > 4. Explain why Marcus is incorrect.', answer: 'With equal numerators, larger denominator means smaller pieces. 3/4 > 3/8.', hint: 'Think about what the denominator tells you about the size of each piece.' },
            { stem: 'Place -2.5, 1/3, and 0.75 on the same number line. Which is closest to zero?', answer: '1/3 is closest to zero (about 0.33)', hint: 'Convert all to decimals, then place them.' }
        ],
        dok3: [
            { stem: 'Create three different fractions between 2/5 and 3/5. Explain your strategy.', answer: 'E.g., 9/20, 1/2, 11/20. Strategy: find equivalent fractions with common denominator.', hint: 'Convert to twentieths: 8/20 and 12/20. What goes between?' }
        ]
    },

    'equivalence and representations': {
        grade: 6,
        dok1: [
            { stem: 'Convert 3/4 to a decimal.', answer: '0.75', hint: 'Divide 3 by 4.' },
            { stem: 'Write 45% as a fraction in simplest form.', answer: '9/20', hint: '45/100 simplifies by dividing by 5.' },
            { stem: 'Convert 0.125 to a fraction.', answer: '1/8', hint: '125/1000 simplifies.' }
        ],
        dok2: [
            { stem: 'Which is the best deal: 1/3 off, 30% off, or 0.35 off the price?', answer: '0.35 off (35%) is the best deal.', hint: 'Convert all to the same form to compare.' },
            { stem: 'A recipe calls for 0.6 cups of sugar. Express this as a fraction and a percent.', answer: '3/5 cup = 60%', hint: '0.6 = 6/10 = 3/5' }
        ],
        dok3: [
            { stem: 'A store advertises "Buy 2, get 1 free." What percent discount is this per item? Explain.', answer: 'You pay for 2 out of 3 items, so 1/3 off = about 33.3% discount per item.', hint: 'Think about total cost vs. total items.' }
        ]
    },

    'factors primes gcf lcm': {
        grade: 6,
        dok1: [
            { stem: 'List all factors of 36.', answer: '1, 2, 3, 4, 6, 9, 12, 18, 36', hint: 'Check each number 1 through 36.' },
            { stem: 'Is 17 prime or composite?', answer: 'Prime (only factors are 1 and 17)', hint: 'Try dividing by 2, 3, 4...' },
            { stem: 'Find the GCF of 24 and 36.', answer: '12', hint: 'List factors of each, find the largest shared one.' }
        ],
        dok2: [
            { stem: 'Use prime factorization to find the LCM of 12 and 18.', answer: 'LCM = 36 (2^2 x 3^2)', hint: '12 = 2^2 x 3, 18 = 2 x 3^2' },
            { stem: 'Two runners lap a track every 6 and 8 minutes. When will they meet at the start together?', answer: 'After 24 minutes (LCM of 6 and 8)', hint: 'Find the LCM.' }
        ],
        dok3: [
            { stem: 'The GCF of two numbers is 6 and their LCM is 72. If one number is 24, what is the other?', answer: '18 (because GCF x LCM = product of the two numbers: 6 x 72 = 432, 432/24 = 18)', hint: 'Use: GCF x LCM = a x b' }
        ]
    },

    'ratios and rates': {
        grade: 6,
        dok1: [
            { stem: 'Write the ratio of 3 cats to 5 dogs in three ways.', answer: '3:5, 3/5, 3 to 5', hint: 'Ratios can be written with a colon, fraction, or words.' },
            { stem: 'Find the unit rate: 240 miles in 4 hours.', answer: '60 miles per hour', hint: 'Divide 240 by 4.' }
        ],
        dok2: [
            { stem: 'A recipe uses 2 cups flour for 3 dozen cookies. How much flour for 9 dozen?', answer: '6 cups flour', hint: 'Set up a proportion: 2/3 = x/9' },
            { stem: 'Store A: 5 apples for $3. Store B: 8 apples for $5. Which is the better buy?', answer: 'Store A ($0.60/apple) vs Store B ($0.625/apple). Store A is better.', hint: 'Calculate the unit price at each store.' }
        ],
        dok3: [
            { stem: 'A map scale is 1 inch = 25 miles. Two cities are 3.5 inches apart on the map. Your car gets 30 mpg and gas costs $3.50/gallon. How much will the trip cost in gas?', answer: '87.5 miles / 30 mpg = 2.917 gal x $3.50 = $10.21', hint: 'First find actual distance, then gallons needed, then cost.' }
        ]
    },

    'multiplication and division of fractions': {
        grade: 6,
        dok1: [
            { stem: 'Multiply: 2/3 x 4/5', answer: '8/15', hint: 'Multiply numerators, multiply denominators.' },
            { stem: 'Divide: 3/4 / 1/2', answer: '3/2 or 1 1/2', hint: 'Invert the second fraction and multiply.' },
            { stem: 'What is 1/3 of 24?', answer: '8', hint: 'Multiply 24 by 1/3.' }
        ],
        dok2: [
            { stem: 'A board is 5/6 foot long. You cut it into pieces that are 1/12 foot each. How many pieces?', answer: '10 pieces (5/6 / 1/12 = 10)', hint: 'Divide the total length by the piece length.' },
            { stem: 'Draw an area model showing 2/3 x 3/4. What fraction of the whole is shaded?', answer: '6/12 = 1/2 of the whole is shaded.', hint: 'Draw a rectangle, divide into thirds one way and fourths the other.' }
        ],
        dok3: [
            { stem: 'A recipe calls for 3/4 cup sugar. You want to make 2/3 of the recipe. Your only measuring cup is 1/8 cup. How many scoops?', answer: '3/4 x 2/3 = 1/2 cup. Then 1/2 / 1/8 = 4 scoops.', hint: 'First find how much sugar, then figure out scoops.' }
        ]
    },

    'percent': {
        grade: 6,
        dok1: [
            { stem: 'What is 25% of 80?', answer: '20', hint: '0.25 x 80' },
            { stem: 'Convert 3/5 to a percent.', answer: '60%', hint: '3 / 5 = 0.6 = 60%' }
        ],
        dok2: [
            { stem: 'A shirt costs $40 and is 15% off. What is the sale price?', answer: '$34 (discount = $6)', hint: '15% of 40 = 6' },
            { stem: 'You scored 18 out of 24. What percent did you get?', answer: '75%', hint: '18/24 = 3/4 = 0.75' }
        ],
        dok3: [
            { stem: 'A store marks up items 40%, then puts them on sale for 25% off. Is the final price more or less than the original cost? By how much percent?', answer: 'Final = 1.40 x 0.75 = 1.05 = 5% more than original cost.', hint: 'Apply markup first, then discount.' }
        ]
    },

    // ======================== GRADE 7 ========================

    'proportional relationships': {
        grade: 7,
        dok1: [
            { stem: 'Is y = 3x a proportional relationship?', answer: 'Yes, it passes through the origin with k = 3.', hint: 'Proportional relationships have the form y = kx.' },
            { stem: 'Find the constant of proportionality: y = 7x.', answer: 'k = 7', hint: 'In y = kx, k is the constant.' }
        ],
        dok2: [
            { stem: 'A car travels 180 miles on 6 gallons. Write the equation and predict miles for 10 gallons.', answer: 'y = 30x; 300 miles for 10 gallons.', hint: 'Find the unit rate first.' },
            { stem: 'Does this table show a proportional relationship? x: 2, 4, 6 / y: 5, 10, 16', answer: 'No. 5/2 = 2.5, 10/4 = 2.5, but 16/6 ≈ 2.67. Ratios are not constant.', hint: 'Check if y/x is the same for all pairs.' }
        ],
        dok3: [
            { stem: 'Two phone plans: Plan A charges $0.10/text. Plan B charges $5/month + $0.05/text. At how many texts are they equal? Which is proportional?', answer: '0.10t = 5 + 0.05t → 0.05t = 5 → t = 100 texts. Plan A is proportional (passes through origin).', hint: 'Set the costs equal and solve.' }
        ]
    },

    'circumference and area of circles': {
        grade: 7,
        dok1: [
            { stem: 'Find the circumference of a circle with radius 5 cm. Use π ≈ 3.14.', answer: 'C = 2πr = 31.4 cm', hint: 'C = 2πr' },
            { stem: 'Find the area of a circle with diameter 10 inches.', answer: 'A = π(5)² = 78.5 sq in', hint: 'Radius = diameter/2. A = πr²' }
        ],
        dok2: [
            { stem: 'A circular garden has circumference 62.8 feet. What is its area?', answer: 'C = 2πr → r = 10 ft → A = π(10)² = 314 sq ft', hint: 'Use circumference to find radius first.' },
            { stem: 'A pizza has diameter 14 inches. Each slice is 1/8 of the pizza. What is the area of one slice?', answer: 'A = π(7)²/8 = 153.94/8 = 19.24 sq in', hint: 'Find total area, then divide by 8.' }
        ],
        dok3: [
            { stem: 'A running track is made of two straight sections (100m each) and two semicircles. The total distance is 400m. What is the diameter of each semicircle?', answer: 'Semicircles total = 400 - 200 = 200m → Full circle circumference = 200m → d = 200/π ≈ 63.66m', hint: 'The two semicircles make one full circle.' }
        ]
    },

    'similarity and scaling': {
        grade: 7,
        dok1: [
            { stem: 'A scale drawing uses 1 cm = 5 m. A room is 3 cm on the drawing. What is the actual length?', answer: '15 m', hint: 'Multiply by the scale factor.' },
            { stem: 'Two triangles are similar. The scale factor is 2:3. If the small triangle has a side of 8 cm, what is the corresponding side?', answer: '12 cm', hint: '8 x 3/2 = 12' }
        ],
        dok2: [
            { stem: 'A photo is 4 in x 6 in. You want to enlarge it to fit a frame that is 10 in wide. What should the height be to keep it proportional?', answer: '15 in (scale factor = 10/4 = 2.5, so 6 x 2.5 = 15)', hint: 'Find the scale factor from the width.' },
            { stem: 'Triangle ABC ~ Triangle DEF. AB = 6, BC = 8, AC = 10. If DE = 9, find EF and DF.', answer: 'Scale = 9/6 = 1.5. EF = 12, DF = 15.', hint: 'Find the scale factor, then multiply each side.' }
        ],
        dok3: [
            { stem: 'A map has scale 1:50,000. You measure a lake as 4.2 cm long and 2.8 cm wide (approximating as an ellipse). Estimate the real area of the lake.', answer: 'Real: 2100m x 1400m. Ellipse area ≈ π(1050)(700) ≈ 2,309,070 m² ≈ 2.31 km²', hint: 'Convert dimensions first, then use ellipse area formula.' }
        ]
    },

    'representing and comparing rational numbers': {
        grade: 7,
        dok1: [
            { stem: 'Plot -3, 1.5, and -0.5 on a number line.', answer: 'Order: -3, -0.5, 1.5', hint: 'Negative numbers go left of zero.' },
            { stem: 'Which is greater: -4 or -7?', answer: '-4 > -7', hint: 'On a number line, -4 is to the right of -7.' }
        ],
        dok2: [
            { stem: 'The temperature was -8°F at 6 AM and rose 15 degrees by noon. Then it dropped 5 degrees by 6 PM. What was the temperature at 6 PM?', answer: '-8 + 15 - 5 = 2°F', hint: 'Add the rise, subtract the drop.' },
            { stem: 'Order from least to greatest: -2/3, -0.5, -3/4, 0.1', answer: '-3/4, -2/3, -0.5, 0.1', hint: 'Convert to decimals: -0.75, -0.667, -0.5, 0.1' }
        ],
        dok3: [
            { stem: 'A submarine is at -200 feet. It rises 50 feet, then dives 3 times as far as it rose. Express its final depth as a rational number and explain.', answer: '-200 + 50 - 150 = -300 feet. The submarine ended deeper because it dove 3x as far as it rose.', hint: 'Track each movement step by step.' }
        ]
    },

    'applying rational numbers': {
        grade: 7,
        dok1: [
            { stem: 'Calculate: -5 + 8', answer: '3', hint: 'Start at -5, move 8 right.' },
            { stem: 'Find: |−12|', answer: '12', hint: 'Absolute value is always positive.' },
            { stem: 'Calculate: (-3)(-4)', answer: '12', hint: 'Negative times negative equals positive.' }
        ],
        dok2: [
            { stem: 'A bank account has $150. You write checks for $45, $72, and $50. What is the balance?', answer: '150 - 45 - 72 - 50 = -$17 (overdrawn)', hint: 'Subtract each check from the balance.' },
            { stem: 'The distance between two points on a number line is |a - b|. Find the distance between -8 and 5.', answer: '|-8 - 5| = |-13| = 13', hint: 'Subtract and take absolute value.' }
        ],
        dok3: [
            { stem: 'A game show: +10 for correct, -15 for wrong, -5 for no answer. After 20 questions (12 correct, 5 wrong, 3 no answer), what is the score?', answer: '12(10) + 5(-15) + 3(-5) = 120 - 75 - 15 = 30 points', hint: 'Multiply each type by its point value, then add.' }
        ]
    },

    'mean median and range': {
        grade: 7,
        dok1: [
            { stem: 'Find the mean of: 12, 15, 18, 21, 24', answer: 'Mean = 90/5 = 18', hint: 'Add all values, divide by count.' },
            { stem: 'Find the median of: 7, 3, 9, 1, 5', answer: 'Median = 5 (ordered: 1, 3, 5, 7, 9)', hint: 'Order the numbers, pick the middle one.' }
        ],
        dok2: [
            { stem: 'Your test scores are 85, 90, 78, 92. What score do you need on the 5th test to average 88?', answer: '88 x 5 = 440. Current total = 345. Need 440 - 345 = 95.', hint: 'Set up: (sum + x)/5 = 88' },
            { stem: 'Data set A: mean 75, range 20. Data set B: mean 75, range 50. Compare them.', answer: 'Same center but B has much more spread/variability.', hint: 'Range tells you about spread.' }
        ],
        dok3: [
            { stem: 'Create a data set of 7 numbers where the mean is 10, the median is 8, and the range is 15.', answer: 'E.g., 3, 5, 7, 8, 12, 17, 18 (mean = 70/7 = 10, median = 8, range = 15)', hint: 'Start with median = 8 in the middle, then build around it.' }
        ]
    },

    // ======================== GRADE 8 ========================

    'rational irrational and real numbers': {
        grade: 8,
        dok1: [
            { stem: 'Classify as rational or irrational: √16', answer: 'Rational (√16 = 4)', hint: 'Is it a perfect square?' },
            { stem: 'Estimate √50 to the nearest whole number.', answer: '7 (since 7² = 49)', hint: '7² = 49, 8² = 64' }
        ],
        dok2: [
            { stem: 'Place √20 on a number line between two consecutive integers. Justify your placement.', answer: 'Between 4 and 5 (4² = 16, 5² = 25), closer to 4 since 20 is closer to 16.', hint: 'Find which perfect squares √20 falls between.' },
            { stem: 'Is 0.121121112... rational or irrational? Explain.', answer: 'Irrational. The pattern grows (not repeating) so it cannot be expressed as a fraction.', hint: 'Rational decimals either terminate or repeat.' }
        ],
        dok3: [
            { stem: 'Prove that √2 is irrational by explaining why it cannot be written as a/b in simplest form.', answer: 'If √2 = a/b, then 2 = a²/b², so a² = 2b². This means a² is even, so a is even (a=2k). Then 4k² = 2b², so b² = 2k², making b even too. But both can\'t be even if a/b is in simplest form. Contradiction.', hint: 'Assume it IS rational and find a contradiction.' }
        ]
    },

    'pythagorean theorem': {
        grade: 8,
        dok1: [
            { stem: 'Find c if a = 3 and b = 4.', answer: 'c = 5 (3² + 4² = 9 + 16 = 25, √25 = 5)', hint: 'a² + b² = c²' },
            { stem: 'Is a triangle with sides 5, 12, 13 a right triangle?', answer: 'Yes (5² + 12² = 25 + 144 = 169 = 13²)', hint: 'Check if a² + b² = c²' }
        ],
        dok2: [
            { stem: 'A ladder leans against a wall, 12 ft from the base. The ladder is 15 ft long. How high up the wall does it reach?', answer: '15² - 12² = 225 - 144 = 81, √81 = 9 ft', hint: 'The ladder is the hypotenuse.' },
            { stem: 'Find the distance between points (1, 2) and (4, 6).', answer: 'd = √((4-1)² + (6-2)²) = √(9+16) = √25 = 5', hint: 'Use the distance formula (derived from Pythagorean theorem).' }
        ],
        dok3: [
            { stem: 'A rectangular park is 300m by 400m. A path goes diagonally. If you walk the diagonal vs. two sides, how much shorter is the diagonal? What percent shorter?', answer: 'Diagonal = 500m. Two sides = 700m. Savings = 200m = 28.6% shorter.', hint: '300² + 400² = c²' }
        ]
    },

    'solve equations inequalities and systems': {
        grade: 8,
        dok1: [
            { stem: 'Solve: 3x + 7 = 22', answer: 'x = 5', hint: 'Subtract 7, then divide by 3.' },
            { stem: 'Solve: 2x - 5 > 9', answer: 'x > 7', hint: 'Add 5, then divide by 2.' }
        ],
        dok2: [
            { stem: 'Solve the system: y = 2x + 1 and y = -x + 7', answer: '2x + 1 = -x + 7 → 3x = 6 → x = 2, y = 5. Solution: (2, 5)', hint: 'Set the equations equal to each other.' },
            { stem: 'A movie costs $12/adult and $8/child. A group of 15 paid $148. How many adults and children?', answer: '12a + 8c = 148, a + c = 15 → a = 7, c = 8', hint: 'Set up two equations and solve.' }
        ],
        dok3: [
            { stem: 'Create a real-world problem that requires a system of equations where the solution is (3, 5). Write and solve it.', answer: 'E.g., Pencils cost $2 and pens cost $3. You buy some of each, spending $21 on 8 items. 2x + 3y = 21, x + y = 8 → x = 3, y = 5.', hint: 'Work backwards from the solution.' }
        ]
    }
};

// ==================== SENTENCE FRAMES DATABASE ====================
// ELL scaffolding sentence frames organized by math activity type
// Used for discussion slides and team collaboration prompts
// ===================================================================

const SENTENCE_FRAMES = {
    problem_solving: [
        "I think the answer is _____ because _____.",
        "First, I will _____, then I will _____.",
        "The problem is asking me to find _____.",
        "I know that _____, so I can _____.",
        "My strategy is to _____ because _____."
    ],
    comparing: [
        "_____ is greater/less than _____ because _____.",
        "These are similar because they both _____.",
        "The difference between _____ and _____ is _____.",
        "I notice that _____ while _____ is different because _____."
    ],
    explaining: [
        "I agree/disagree with _____ because _____.",
        "Another way to think about this is _____.",
        "This makes sense because _____.",
        "The pattern I see is _____.",
        "I can prove this by _____."
    ],
    vocabulary: [
        "_____ means _____. An example is _____.",
        "_____ and _____ are related because _____.",
        "In my own words, _____ means _____.",
        "I used _____ (vocab word) when I _____."
    ],
    reflection: [
        "Today I learned that _____.",
        "I used to think _____, but now I know _____.",
        "Something I still wonder about is _____.",
        "The most important idea from today is _____.",
        "I feel confident about _____ but need more practice with _____."
    ]
};

// ==================== TEAM ROLE PROMPTS ====================
// Context-specific prompts for each team role during math activities
// ===============================================================

const TEAM_ROLE_PROMPTS = {
    problem_launch: {
        facilitator: [
            "Who wants to read the problem aloud?",
            "What do we need to do to get started?",
            "Let's make sure everyone understands before we begin."
        ],
        resource_manager: [
            "What materials do we need?",
            "What are we supposed to figure out?",
            "Do we need to ask the teacher anything?"
        ],
        task_manager: [
            "What should we try first?",
            "Do we all agree on our approach?",
            "We have _____ minutes — let's stay on track."
        ],
        recorder_reporter: [
            "I'll write down our work and thinking.",
            "What are we going to say to the class?",
            "Let me record what _____ said."
        ]
    },
    discussion: {
        facilitator: [
            "Who has an idea to share?",
            "_____, what do you think?",
            "Does everyone agree, or does someone see it differently?"
        ],
        resource_manager: [
            "What information do we have?",
            "What do we still need to know?",
            "Can someone explain that in another way?"
        ],
        task_manager: [
            "Are we answering the right question?",
            "Let's check our work before moving on.",
            "Are we ready for the next part?"
        ],
        recorder_reporter: [
            "So our answer is _____ because _____.",
            "I'll present: we found that _____.",
            "Let me summarize what we discussed."
        ]
    }
};

// ==================== HELPER FUNCTIONS ====================

/**
 * Get DOK problems for detected topics
 * @param {string[]} topics - Array of detected topic names
 * @returns {object} { topic: string, problems: { dok1: [], dok2: [], dok3: [] } }[]
 */
function getLeveledProblems(topics) {
    const results = [];
    for (const topic of topics) {
        // Exact match
        if (DOK_PROBLEMS[topic]) {
            results.push({ topic, problems: DOK_PROBLEMS[topic] });
            continue;
        }
        // Fuzzy match: check if any DOK key is contained in topic or vice versa
        const tLower = topic.toLowerCase();
        for (const [key, data] of Object.entries(DOK_PROBLEMS)) {
            if (tLower.includes(key) || key.includes(tLower)) {
                results.push({ topic, problems: data });
                break;
            }
            // Word overlap
            const tWords = tLower.split(/\s+/);
            const kWords = key.split(/\s+/);
            const overlap = tWords.filter(w => w.length > 3 && kWords.includes(w));
            if (overlap.length >= 2) {
                results.push({ topic, problems: data });
                break;
            }
        }
    }
    return results;
}

/**
 * Get sentence frames relevant to detected activity types
 * @param {object[]} slides - Array of classified slides
 * @returns {object} Categorized sentence frames relevant to the lesson
 */
function getRelevantSentenceFrames(slides) {
    const types = slides.map(s => s.type);
    const frames = {};

    // Always include problem solving and explaining
    frames.problem_solving = SENTENCE_FRAMES.problem_solving;
    frames.explaining = SENTENCE_FRAMES.explaining;

    // Add comparing if there are comparison-related slides
    if (types.some(t => ['PROBLEM_SLIDE', 'NOTICE_WONDER', 'WOULD_YOU_RATHER'].includes(t))) {
        frames.comparing = SENTENCE_FRAMES.comparing;
    }

    // Add vocabulary if vocabulary cards detected or teaching insights have terms
    frames.vocabulary = SENTENCE_FRAMES.vocabulary;

    // Always include reflection for closure
    frames.reflection = SENTENCE_FRAMES.reflection;

    return frames;
}

/**
 * Get role prompts based on slide types present
 * @param {object[]} slides - Array of classified slides
 * @returns {object} Role prompts for problem launch and discussion
 */
function getRelevantRolePrompts(slides) {
    const prompts = {};
    const types = slides.map(s => s.type);

    if (types.some(t => ['PROBLEM_SLIDE', 'ACTIVITY_LAUNCH', 'FOCUS_SKILL_DETAIL'].includes(t))) {
        prompts.problem_launch = TEAM_ROLE_PROMPTS.problem_launch;
    }
    if (types.some(t => ['GROUP_DISCUSSION', 'STORY_MISSION', 'CLOSURE', 'NOTICE_WONDER'].includes(t))) {
        prompts.discussion = TEAM_ROLE_PROMPTS.discussion;
    }

    // Default: include both
    if (Object.keys(prompts).length === 0) {
        prompts.problem_launch = TEAM_ROLE_PROMPTS.problem_launch;
        prompts.discussion = TEAM_ROLE_PROMPTS.discussion;
    }

    return prompts;
}
