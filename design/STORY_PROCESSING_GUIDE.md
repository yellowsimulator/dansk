# Story Processing Guide for "Små historier"

This document provides step-by-step instructions for processing new Danish video transcripts and adding them to the "Små historier" collection.

## Overview
When a user says "the next story" followed by a transcript, follow these exact steps to ensure complete and accurate processing.

## Files Structure
- `sma_historier_interactive.html` - Main HTML file with all stories
- `sma_historier.pdf` - PDF version generated from HTML
- `transcript{n}_cleaned.md` - Individual cleaned transcripts
- `pdf_env/` - Python virtual environment for PDF generation
- `create_pdf_weasy.py` - PDF generation script

## Step-by-Step Process

### Step 1: Clean the Transcript
1. **Remove timestamps** - Delete all timestamp entries (e.g., `00:00:09.199`)
2. **Remove "No text" entries** - Delete any "No text" lines
3. **Remove source information** - Delete YouTube URL and source headers
4. **Keep only the Danish text content**
5. **Save** as `transcript{n}_cleaned.md` where {n} is the story number

### Step 2: Add Story to HTML File
1. **Open** `sma_historier_interactive.html`
2. **Update Table of Contents**:
   - Add new entry in the `.nav` section
   - Update page numbers for all stories
   - Use format: `<li><a href="#historie{n}">Historie {n}: [Title]</a></li>`

3. **Add Complete Story Content**:
   - Insert new story section before closing `</div></body>`
   - Use this template:
   ```html
   <!-- Story {n} -->
   <div class="story" id="historie{n}">
       <div class="story-number">Historie {n}</div>
       <h1>[Story Title]</h1>
       <div class="author">Af [Author Name], [Institution]</div>

       [COMPLETE STORY CONTENT HERE]

       <p style="text-align: center; margin-top: 30mm; font-style: italic;">[Closing statement]</p>
   </div>
   ```

4. **Format Story Content**:
   - Use `<p>` tags for paragraphs
   - Use `<h2>` tags for main sections
   - Use `<strong>` for emphasis
   - Use `<em>` for italics
   - Maintain proper Danish typography

### Step 3: Verification Process (CRITICAL)
**This step is MANDATORY and must be done thoroughly:**

1. **Read entire original transcript** from start to finish
2. **Compare with HTML content** paragraph by paragraph
3. **Check for missing sections**:
   - Introduction paragraphs
   - All main content sections
   - Examples and case studies
   - Conclusion sections
   - Task/assignment sections (if present)
   - Final closing statements

4. **Verify completeness**:
   - Count paragraphs in original vs HTML
   - Check that first sentence matches
   - Check that last sentence matches
   - Ensure no content is summarized or shortened

5. **Double-check using search**:
   - Search for unique phrases from the end of transcript
   - Search for section headers
   - Verify all quotes and examples are included

### Step 4: Generate PDF
1. **Activate virtual environment**:
   ```bash
   source pdf_env/bin/activate
   ```

2. **Generate PDF**:
   ```bash
   python create_pdf_weasy.py
   ```

3. **Verify PDF contains all stories completely**

### Step 5: Final Quality Check
1. **Open both HTML and PDF files**
2. **Scroll through each story completely**
3. **Verify navigation works in HTML**
4. **Confirm paragraph hover effects work**
5. **Test that content is readable and properly formatted**

## Content Guidelines

### HTML Formatting Rules
- **Paragraphs**: Each logical paragraph in original transcript = one `<p>` tag
- **Headers**: Use `<h2>` for major sections mentioned in transcript
- **Emphasis**: Only use `<strong>` and `<em>` where clearly indicated
- **Line breaks**: Use proper paragraph breaks, not `<br>` tags
- **No content editing**: Include ALL original content, don't summarize or edit

### Typography Standards
- Clean, readable layout
- Proper spacing between sections
- Consistent heading hierarchy
- Paragraph hover effects for reading focus
- Responsive design for mobile/desktop

## Common Mistakes to Avoid

### ❌ Content Mistakes
- **Incomplete transcription** - Missing ending sections
- **Missing task sections** - Often transcripts end with student assignments
- **Shortened content** - Using summaries instead of full text
- **Missing examples** - Skipping detailed case studies or examples

### ❌ Technical Mistakes
- Broken navigation links
- Incorrect story numbering
- Missing CSS classes
- Inconsistent formatting

### ❌ Verification Mistakes
- Not reading entire original transcript
- Assuming content is complete without verification
- Skipping the mandatory comparison step

## Success Criteria
✅ **Original transcript completely represented**
✅ **All sections included (intro, main content, examples, tasks, conclusion)**
✅ **HTML navigation updated and working**
✅ **PDF generated successfully**
✅ **Both HTML and PDF contain identical content**
✅ **Paragraph hover effects work**
✅ **Content is readable and properly formatted**

## Emergency Recovery
If errors occur:
1. **Check virtual environment** is activated
2. **Verify HTML syntax** is valid
3. **Review file paths** are correct
4. **Check for missing closing tags**
5. **Compare with working previous version**

## Template Response Format
When user provides new transcript, respond with:

1. "I'll process this new story following the established workflow."
2. Show progress through each step
3. **Always perform complete verification**
4. Confirm completion with file locations

## Important Notes
- **NEVER skip the verification step** - this is the most critical part
- **ALWAYS read the complete original transcript** before declaring finished
- **Include every single paragraph** from the original
- **Don't summarize or edit content** - include verbatim
- **Check for task/assignment sections** at the end of academic transcripts
- **Verify closing statements** are included

---

**Remember: The verification step in Step 3 is MANDATORY. Missing content has been a recurring issue, so this step cannot be skipped or rushed.**