# ✅ RuleMiner Prompt - Integration Complete

**Date:** 2025-10-31  
**Status:** ✅ Integrated into Prompt Arsenal

---

## 🎯 What Was Created

Successfully integrated the **RuleMiner** prompt into the Arsenal ecosystem - a systematic tool for extracting actionable, repo-specific Rules from Cascade conversations and workspace knowledge.

### **File Created**
**Location:** `prompt-arsenal/meta-prompting/ruleminer-extract-rules.md`

**Size:** 10,000+ words of comprehensive documentation

---

## 📊 What RuleMiner Does

**Purpose:** Extract practical, non-obvious Rules from:
- Current Cascade conversation threads
- Workspace files and configurations
- Existing rules (global and workspace)
- External framework conventions

**Output:** 8-20 curated, actionable Rules with:
- ✅ Activation modes (Always On, Manual, Model Decision, Glob)
- ✅ Storage location recommendations
- ✅ Evidence and confidence scores (0.0-1.0)
- ✅ Concrete playbooks for future use
- ✅ Anti-patterns to avoid

---

## 🎯 Key Features

### **1. Systematic Extraction Process**

**4-Step Method:**
1. **Harvest evidence** - Mine thread + scan workspace + load existing rules + check @web
2. **Propose candidates** - Generate 15-40 rules, score on 4 dimensions
3. **Deduplicate & filter** - Merge duplicates, keep top 8-20 by score
4. **Finalize with activation** - Assign modes and storage locations

### **2. Quality Scoring System**

Each rule scored on 4 dimensions (1-5 scale):
- **Impact** - Prevents critical bugs or major inconsistencies
- **Recurrence** - How often it applies
- **Clarity** - How actionable the playbook is
- **Repo-Specificity** - Unique to this codebase vs generic

**Keep rules with:** Total score ≥ 12 (out of 20)

### **3. Structured Output Format**

```markdown
### <Rule Title>
**Category:** (Architecture | Code Style | Testing | API | Security | ...)
**Rule:** <short bullets with instructions>
**When to apply:** <conditions + Activation Mode suggestion>
**Why this is good:** <1-3 bullets with evidence>
**How to use in the future (playbook):** <concrete steps>
**Anti-patterns:** <common mistakes to avoid>
**Evidence:** <file paths, commits, thread URLs>
**Confidence:** <0.0-1.0>
```

### **4. Activation Mode Recommendations**

- **Always On** - Fundamental standards everywhere
- **Manual** - Niche instructions via `@mention`
- **Model Decision** - Natural-language condition
- **Glob** - File patterns (`api/**/*.ts`, `**/*.py`)

---

## 💡 How to Use

### **Basic Usage**

```
[After completing significant work in Cascade]

[Paste RuleMiner prompt]
```

Cascade will analyze and extract 8-20 actionable rules.

### **With Context**

```
[Paste RuleMiner prompt]

Additional context:
- Focus on: API design rules
- Stack: Next.js + FastAPI + PostgreSQL
- Team: 5 developers
- Priority: Security and consistency
```

### **Integration with Complete-Mode**

```
@complete-mode
Task = Implement payment processing feature
Context = Stripe integration; critical revenue path

[DONE overlay — Software/DevOps]
strict:on

[After completion, run RuleMiner to extract rules]
```

---

## 🎓 Use Cases

### **1. After Major Features**
Extract patterns from complex implementations
- **Input:** 2-week feature implementation thread
- **Output:** 12 rules (API design, testing, security, performance)
- **Value:** Codify decisions, prevent future inconsistencies

### **2. Post-Incident Analysis**
Capture lessons learned from bugs/incidents
- **Input:** Production incident resolution thread
- **Output:** 8 rules (monitoring, error handling, incident response)
- **Value:** Prevent recurrence, improve reliability

### **3. Onboarding New Team Members**
Extract implicit team knowledge
- **Input:** Entire codebase scan
- **Output:** 15 rules (code style, architecture, testing, deployment)
- **Value:** Faster onboarding, consistent standards

### **4. Codebase Audits**
Identify inconsistencies and standardize
- **Input:** Multi-week refactoring effort
- **Output:** 20 rules across all categories
- **Value:** Improved consistency, reduced tech debt

### **5. Framework Migrations**
Document new patterns during transitions
- **Input:** Migration from Pages Router to App Router
- **Output:** 10 rules (new patterns, deprecated approaches)
- **Value:** Guide team through transition

---

## 🔄 Integration with Arsenal Ecosystem

### **Works With**

**1. Prompt Forensics Analyzer**
```
# Full knowledge extraction workflow
1. Prompt Forensics Analyzer → Extract prompts/patterns
2. RuleMiner → Extract rules
3. Result: Comprehensive knowledge capture
```

**2. Complete Problem-Solving Rule**
```
@complete-mode
[Complete rigorous work]

[Then run RuleMiner to extract rules from the process]
```

**3. Insights Extraction Pipeline**
```
1. Complete feature work
2. Run Prompt Forensics Analyzer (extract prompts)
3. Run RuleMiner (extract rules)
4. Run Insights Intake Processor (categorize)
5. Update Arsenal repositories
```

**4. Enterprise Completion Standards**
```
# Extract team-specific DONE criteria
[Run RuleMiner after several complete-mode sessions]
[Extract patterns → Update enterprise-completion-standards-memory.md]
```

---

## 📈 Success Metrics

### **Quality Indicators**

**Good RuleMiner Output:**
- ✅ 8-20 rules (not too few, not overwhelming)
- ✅ Average confidence ≥0.7
- ✅ Repo-specific (not generic)
- ✅ Actionable playbooks
- ✅ Evidence-based

**Poor RuleMiner Output:**
- ❌ Generic rules ("write good code")
- ❌ Too many rules (>30)
- ❌ Low confidence (<0.5 average)
- ❌ Vague instructions
- ❌ No evidence

### **Impact Metrics**

**Track:**
- Rules extracted per session
- Rules implemented (vs proposed)
- Reduction in recurring issues
- Onboarding time improvement
- Code consistency scores

---

## 📚 Real-World Examples

### **Example 1: API Refactor**

**Context:** 2-day authentication API refactor

**Output:** 12 rules
- 4 API design rules (response envelopes, error codes)
- 3 Security rules (token storage, rotation, validation)
- 2 Testing rules (auth flow coverage, edge cases)
- 2 Database rules (session cleanup, indexing)
- 1 Documentation rule (API changelog)

**Files Created:**
- `.windsurf/rules/api-auth-standards.md` (Always On)
- `.windsurf/rules/security-tokens.md` (Glob `api/auth/**/*.ts`)

### **Example 2: Production Incident**

**Context:** Payment webhook race condition

**Output:** 8 rules
- 3 Payment processing rules (idempotency, webhooks, retries)
- 2 Monitoring rules (alerts, logging)
- 2 Testing rules (integration tests, load tests)
- 1 Incident response rule (runbook updates)

**Files Created:**
- `.windsurf/rules/payment-processing.md` (Glob `api/payments/**/*.ts`)
- `.windsurf/rules/incident-prevention.md` (Always On)

### **Example 3: Team Onboarding**

**Context:** New developer joining

**Output:** 15 rules
- 5 Code style rules (naming, imports, file organization)
- 4 Architecture rules (folder structure, module boundaries)
- 3 Testing rules (coverage, test organization, mocking)
- 2 Deployment rules (CI/CD, environment variables)
- 1 Documentation rule (README standards)

**Files Created:**
- `.windsurf/rules/code-style.md` (Always On)
- `.windsurf/rules/architecture.md` (Always On)
- `.windsurf/rules/testing-standards.md` (Glob `**/*.test.ts`)
- `global_rules.md` (updated)

---

## 🔗 Related Arsenal Items

### **Prompts**
- [Prompt Forensics Analyzer](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/meta-prompting/prompt-forensics-analyzer.md) - Extract prompts
- [Insights Intake Processor](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/meta-prompting/insights-intake-processor.md) - Process insights
- [Self-Score Output](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/quality-assurance/self-score-output.md) - Validate quality

### **Memories**
- [Prompt Patterns Library](https://github.com/ChrisTansey007/windsurf-memories-arsenal) - Store patterns
- [Enterprise Completion Standards](https://github.com/ChrisTansey007/windsurf-memories-arsenal) - Team standards

### **Rules**
- [Prompt Quality Standards](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/prompt-design/prompt-quality-standards.md) - Quality framework
- [Complete Problem-Solving](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/by-domain/complete-problem-solving.md) - Rigorous completion

### **Workflows**
- [Insights Extraction Pipeline](https://github.com/ChrisTansey007/ai-workflows-arsenal) - Complete workflow

### **Examples**
- [Meta-Prompting Example](https://github.com/ChrisTansey007/arsenal-integration-hub/tree/main/examples/meta-prompting) - Full setup

---

## 💡 Pro Tips

### **1. Run After Significant Work**
More context = better rules

### **2. Combine with Other Meta-Prompts**
```
1. Prompt Forensics Analyzer → Prompts
2. RuleMiner → Rules
3. Self-Score Output → Validation
```

### **3. Customize for Your Domain**
```
Additional context:
- Focus on: Security (healthcare domain)
- Compliance: HIPAA required
- Team: 5 developers, 2 juniors
```

### **4. Iterate on Low-Confidence Rules**
If confidence <0.7, gather more evidence and re-run

### **5. Create Rule Collections**
Extract rules by category over time:
- Week 1: API rules
- Week 2: Testing rules
- Week 3: Security rules
- Week 4: Performance rules

---

## ⚠️ Limitations

**1. Context Window**
- Only analyzes current thread + workspace
- May miss historical context
- **Mitigation:** Run periodically

**2. Subjectivity**
- Some rules may be controversial
- Confidence scores help identify uncertain rules
- **Mitigation:** Review with team

**3. Duplication Risk**
- May propose similar rules to existing ones
- **Mitigation:** Manual review recommended

---

## 🎯 Quick Reference

**When to use:** After significant work, post-incident, onboarding, audits  
**Output:** 8-20 scored, actionable rules  
**Time:** 5-10 min to run, 20-30 min to review  
**Value:** Codifies knowledge, prevents issues, improves consistency

---

## ✅ Integration Checklist

- [x] **Prompt created** in prompt-arsenal/meta-prompting/
- [x] **YAML front matter** with Arsenal metadata
- [x] **Comprehensive documentation** (10,000+ words)
- [x] **Real-world examples** (3 scenarios)
- [x] **Integration guide** with Arsenal ecosystem
- [x] **Cross-links** to related Arsenal items
- [x] **Pro tips** and best practices
- [x] **Success metrics** and quality indicators
- [x] **Limitations** and considerations
- [x] **Quick reference** guide

---

## 🎉 Success!

**RuleMiner** is now fully integrated into the Arsenal ecosystem and ready to use for systematic rule extraction from conversations and codebases!

---

**Source:** Community contribution  
**Integration Date:** 2025-10-31  
**Status:** Complete ✅  
**License:** MIT (part of Prompt Arsenal)
