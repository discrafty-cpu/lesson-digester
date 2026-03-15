/**
 * ProblemGenerator - Client-side module for generating parametric math problems
 *
 * Uses DOK_PROBLEMS global (from leveled-problems-data.js) as seed templates
 * Creates variations with different numbers while maintaining mathematical structure
 *
 * IIFE pattern with zero external dependencies
 */

const ProblemGenerator = (() => {
  // ============================================================================
  // INTERNAL HELPERS
  // ============================================================================

  /**
   * Generate random integer between min and max (inclusive)
   */
  const randomInt = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  };

  /**
   * Pick random element from array
   */
  const randomChoice = (arr) => {
    if (!arr || arr.length === 0) return null;
    return arr[Math.floor(Math.random() * arr.length)];
  };

  /**
   * Vary a number by shifting it within a range, keeping result positive
   */
  const varyNumber = (n, range) => {
    const shift = randomInt(-range, range);
    return Math.max(1, n + shift);
  };

  /**
   * Generate a valid fraction with reasonable numerator/denominator
   */
  const varyFraction = (num, denom) => {
    const denominators = [2, 3, 4, 5, 6, 8, 10, 12];
    const newDenom = randomChoice(denominators);
    // Keep numerator smaller than denominator (proper fraction)
    const newNum = randomInt(1, Math.max(1, newDenom - 1));
    return { num: newNum, denom: newDenom };
  };

  /**
   * Swap numbers in text with regex, handling various number formats
   * Finds all numbers and replaces them with new numbers
   */
  const swapNumbersInText = (text, oldNumbers, newNumbers) => {
    let result = text;

    // Sort by length descending to replace longer numbers first
    const sorted = oldNumbers
      .map((num, idx) => ({ num, idx }))
      .sort((a, b) => String(b.num).length - String(a.num).length);

    sorted.forEach(({ num, idx }) => {
      if (idx < newNumbers.length) {
        const regex = new RegExp(`\\b${num}\\b`, 'g');
        result = result.replace(regex, newNumbers[idx]);
      }
    });

    return result;
  };

  /**
   * Extract all numbers from text (integers and basic decimals/fractions)
   */
  const extractNumbers = (text) => {
    const matches = text.match(/\d+(?:\.\d+)?/g) || [];
    return matches.map(m => isNaN(m) ? null : parseFloat(m)).filter(n => n !== null);
  };

  /**
   * Get a pool of problems for a topic from DOK_PROBLEMS
   */
  const getProblemsForTopic = (topic) => {
    if (!window.DOK_PROBLEMS || !window.DOK_PROBLEMS[topic]) {
      return null;
    }
    return window.DOK_PROBLEMS[topic];
  };

  /**
   * Generate a generic fallback problem when topic not found
   */
  const generateGenericProblem = (dok) => {
    const operations = ['+', '-', '×', '÷'];
    const op = randomChoice(operations);
    let a, b, answer, stem;

    if (op === '+') {
      a = randomInt(1, 20);
      b = randomInt(1, 20);
      stem = `What is ${a} + ${b}?`;
      answer = a + b;
    } else if (op === '-') {
      a = randomInt(10, 30);
      b = randomInt(1, a - 1);
      stem = `What is ${a} - ${b}?`;
      answer = a - b;
    } else if (op === '×') {
      a = randomInt(2, 12);
      b = randomInt(2, 12);
      stem = `What is ${a} × ${b}?`;
      answer = a * b;
    } else {
      a = randomInt(2, 12);
      b = randomInt(2, 12);
      const product = a * b;
      stem = `What is ${product} ÷ ${b}?`;
      answer = a;
    }

    return {
      stem,
      answer: String(answer),
      hint: `Try ${op} the numbers`,
      dok
    };
  };

  // ============================================================================
  // PUBLIC API
  // ============================================================================

  return {
    /**
     * Get problems for a specific topic and DOK level
     * @param {string} topic - DOK_PROBLEMS topic key
     * @param {number} dok - 1, 2, or 3
     * @param {number} count - How many problems to return
     * @returns {Array} Array of {stem, answer, hint, dok} objects
     */
    forTopic(topic, dok, count) {
      const problems = [];
      const topicData = getProblemsForTopic(topic);

      if (!topicData) {
        // Fallback: generate generic problems
        for (let i = 0; i < count; i++) {
          problems.push(generateGenericProblem(dok));
        }
        return problems;
      }

      const dokKey = `dok${dok}`;
      const seedProblems = topicData[dokKey] || [];

      // First, add seed problems
      for (let i = 0; i < Math.min(seedProblems.length, count); i++) {
        const seed = seedProblems[i];
        problems.push({
          stem: seed.stem,
          answer: seed.answer,
          hint: seed.hint,
          dok
        });
      }

      // Then generate variations if we need more
      while (problems.length < count) {
        const seedProblem = randomChoice(seedProblems);
        if (seedProblem) {
          const variation = this.generateVariation(seedProblem, topic);
          problems.push(variation);
        } else {
          problems.push(generateGenericProblem(dok));
        }
      }

      return problems.slice(0, count);
    },

    /**
     * Get problems for a worksheet level
     * @param {string} topic - DOK_PROBLEMS topic key
     * @param {number} level - 1-6 (Foundational to Advanced)
     * @param {number} count - Total problems to return
     * @returns {Array} Mixed DOK problems appropriate for level
     */
    forLevel(topic, level, count) {
      const problems = [];

      if (level === 1) {
        // Foundational: DOK 1 only
        return this.forTopic(topic, 1, count);
      } else if (level === 2) {
        // Supported: mostly DOK 1, 1 DOK 2
        const split = Math.max(1, count - 1);
        problems.push(...this.forTopic(topic, 1, split));
        if (count > 1) problems.push(...this.forTopic(topic, 2, 1));
      } else if (level === 3) {
        // Scaffolded: DOK 1 + DOK 2 mix
        const split = Math.ceil(count * 0.6);
        problems.push(...this.forTopic(topic, 1, split));
        problems.push(...this.forTopic(topic, 2, count - split));
      } else if (level === 4) {
        // Grade-level: balanced DOK 1 + DOK 2 + DOK 3
        const split1 = Math.ceil(count * 0.4);
        const split2 = Math.ceil(count * 0.4);
        const split3 = count - split1 - split2;
        problems.push(...this.forTopic(topic, 1, split1));
        problems.push(...this.forTopic(topic, 2, split2));
        problems.push(...this.forTopic(topic, 3, split3));
      } else if (level === 5) {
        // Enriched: DOK 2 + DOK 3
        const split = Math.ceil(count * 0.5);
        problems.push(...this.forTopic(topic, 2, split));
        problems.push(...this.forTopic(topic, 3, count - split));
      } else if (level === 6) {
        // Advanced: DOK 3 + open-ended
        const split = Math.ceil(count * 0.7);
        problems.push(...this.forTopic(topic, 3, split));
        // Generate some open-ended variations
        for (let i = 0; i < count - split; i++) {
          const p = this.forTopic(topic, 3, 1)[0];
          if (p) {
            problems.push({
              ...p,
              stem: p.stem + ' Explain your reasoning.'
            });
          }
        }
      }

      return problems.slice(0, count);
    },

    /**
     * Generate a variation of a seed problem with different numbers
     * @param {object} problem - Seed problem {stem, answer, hint}
     * @param {string} topic - Topic name (for context)
     * @returns {object} New problem with varied numbers
     */
    generateVariation(problem, topic) {
      const { stem, answer, hint } = problem;

      // Extract numbers from stem
      const stemNumbers = extractNumbers(stem);
      if (stemNumbers.length === 0) {
        // No numbers to vary, return slightly modified version
        return {
          stem,
          answer,
          hint,
          dok: 1
        };
      }

      // Vary each number in the stem
      const newStemNumbers = stemNumbers.map(n => {
        // Detect if it's likely a fraction denominator (small, 2-12)
        if (n >= 2 && n <= 12 && Math.random() < 0.3) {
          return randomInt(2, 12);
        }
        // Detect if it's a percentage (0-100)
        if (n >= 0 && n <= 100 && String(stem).includes('%')) {
          return randomInt(5, 95);
        }
        // Regular number: vary by 20-30%
        const range = Math.max(1, Math.floor(n * 0.25));
        return varyNumber(n, range);
      });

      // Replace numbers in stem
      let newStem = stem;
      stemNumbers.forEach((oldNum, idx) => {
        const regex = new RegExp(`\\b${oldNum}\\b`, 'g');
        newStem = newStem.replace(regex, newStemNumbers[idx]);
      });

      // Attempt to vary the answer similarly
      let newAnswer = answer;
      const answerNumbers = extractNumbers(answer);
      if (answerNumbers.length > 0) {
        const newAnswerNumbers = answerNumbers.map(n => {
          const range = Math.max(1, Math.floor(n * 0.25));
          return varyNumber(n, range);
        });
        answerNumbers.forEach((oldNum, idx) => {
          const regex = new RegExp(`\\b${oldNum}\\b`, 'g');
          newAnswer = newAnswer.replace(regex, newAnswerNumbers[idx]);
        });
      }

      return {
        stem: newStem,
        answer: newAnswer,
        hint,
        dok: 1
      };
    },

    /**
     * Get a master pool of problems across all DOK levels for a topic
     * Returns ~20 problems (mix of DOK 1, 2, 3)
     * @param {string} topic - DOK_PROBLEMS topic key
     * @returns {Array} Array of problems
     */
    getPool(topic) {
      const problems = [];

      // Get 7-8 from each DOK level
      problems.push(...this.forTopic(topic, 1, 8));
      problems.push(...this.forTopic(topic, 2, 7));
      problems.push(...this.forTopic(topic, 3, 5));

      return problems;
    }
  };
})();
