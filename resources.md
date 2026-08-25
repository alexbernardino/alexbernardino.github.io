---
layout: page
title: Resources
permalink: /resources/
---


# Machine Learning

## Interactive demos

- <a href="https://alexbernardino.github.io/regression-interactive/" target="_blank" rel="noopener noreferrer">Regression interactive demo</a>

- <a href="https://alexbernardino.github.io/knn-interactive/" target="_blank" rel="noopener noreferrer">K Nearest Neighbour interactive demo</a>

---

# Reporting Guidelines

This document describes some guidelines for writing proposals, theses and presentations, and lists common mistakes I find in reports and talks from students.

## Structure and Logic

### Look at examples

Read other good theses and reports of the same type you are aiming at. Try to understand the common structure among them. Do not try to be creative in terms of structure. People are used to a standard order of things, so they are confused if things are out of order.

### Research Canvas

Filling in a research canvas as the one in the link below helps you structure the ideas on your thesis.

<a href="https://www.academic-toolkit.com/sgoisdsf83743msnj23lkisbadnsbj" target="_blank" rel="noopener noreferrer">Research Design Canvas</a>

Start with the Research Design Canvas.

### The Heilmeier’s Questions

These are the key questions you should be able to answer about your project, both in written and verbal form.

- What are you trying to do? Articulate your objectives using absolutely no jargon.
- How is it done today, and what are the limits of current practice?
- What is new in your approach and why do you think it will be successful?
- Who cares? If you are successful, what difference will it make?
- What are the risks?
- How much will it cost?
- How long will it take?
- What are the mid-term and final “exams” to check for success?

## Literature Review

Find the important keywords of your research topic, which may require some iterations, and search for relevant papers in Google Scholar:

<a href="https://scholar.google.com" target="_blank" rel="noopener noreferrer">Google Scholar</a>

Check the prior quality of the papers you read. There are good and bad papers everywhere, but the chance to get bad papers in high ranked conferences and journals is lower. So, beginners should start reading papers on rank A conferences and Q1 journals.

To check the conference ranks you may use:

<a href="http://www.conferenceranks.com" target="_blank" rel="noopener noreferrer">Conference Ranks</a>

To check journals quality factor you may use:

<a href="https://www.scimagojr.com" target="_blank" rel="noopener noreferrer">SCImago Journal & Country Rank</a>

For initial searches and to get an overall view of the research topic, look for recent “survey” or “review” papers on the topic of interest.

Make forward searches. When you find a nice paper and want to know more recent related works, click on the link “cited by ...” that appears below the paper description in Google Scholar.

Some applications, like Mendeley, may help you organize your bibliography.

## Work Plan

In project proposals it is very important to define the work plan.

Identify the tasks that are required to achieve your objectives. Arrange the tasks in a Gantt chart in a temporal logical order. Tasks should go in parallel as much as possible, unless they have some critical dependency on the result of some other task. For example, training an algorithm with a dataset can only start when you have the dataset, but the development of the algorithm can start before the dataset is ready.

The literature survey and thesis writing tasks should run during the whole period. Periodically you should put in the report your progress and search for related works.

You should identify a few milestones in the timeline of your project. Milestones are tangible and verifiable outcomes of your work, that your supervisors may easily check. For example, the finalization of the development of an algorithm is not a milestone because it cannot be verifiable. Just by looking at the code you produced it is not possible to confirm it is finalised. Instead your milestones should be like “Folder with the Dataset”, “Results of the Algorithm Benchmarking”, “Document with Comparison of the Methods”, etc.

The work plan is a live document. During the execution of the project you may need to make adjustments. Always bring your updated work plan to the meetings with your supervisors.

## Writing

### About Figures and Tables

- Always put units and labels in the axes of figures and headers of tables.
- In figures with multiple plots, make sure to insert a legend identifying the different plots.
- Figures and Tables are float objects. We never know where they are to be placed. Never say “in the next figure” or “in the figure above”. Always use proper references.
- All figures and tables should be referred to in the main text. Do not leave them orphans.
- All figures and text must have a succinct self-contained description, or caption, such that a reader can understand it without reading the main text. Describe all symbols in the figure that are not obvious.
- The caption should be complete but only descriptive. Do not make judgements about results, good or bad, here; judgements should go to the main text.
- If your figure has many subfigures, make sure to identify in which aspect they differ, such as different parameters or different conditions.
- If figures contain material from other sources, please identify the source in the caption with a suitable reference.

### About Bibliographic References and Citations

All bibliographic references must have the following fields:

- Name of authors
- Title of the work, such as article, book, or thesis
- Place of publication, such as journal, conference proceedings, editor, or university
- Year

Some publications may have other fields:

- Editor, for journals
- Location, for conference proceedings
- DOI

Most publications that are in public repositories, such as CoRR or arXiv, are also in journals or conferences. Please cite the journal/conference version instead of the repository one, since that is more informative about the scope and quality of the work.

When mentioning the work of others, use “in that work” instead of “in this work”. The expression “in this work” is reserved to the current work. So, use “in that work” to make indirect references to the work of others.

Examples for citing works:

- “In [4] it is proposed a segmentation network to detect people.”
- “Several works, e.g. [45][32][12], have addressed that problem using saliency detection methods [6].”
- “The model for infrared cameras is given by [5]: <write the equation>.”
- In figure captions: “Diagram of the Segmentation network. Adapted from [43].”

Avoid citing works like this:

- Starting a sentence with a reference: “[6] presents a method for segmentation.”
- Making a big paragraph with a lot of information and putting the citation in the end. Citations should come early.

### About Equations

- After each equation explain all symbols in the equation not previously defined.
- Equations are part of the sentences. If the text after the equation is still explaining the equation, it should not appear indented. If the equation finalizes a sentence, use a period at the end of the equation.
- Equation numbers should always be inside curved brackets, as they appear in the right of the equation definition.
- When referring to an equation, e.g. (3.2), you do not need to write “Equation (3.2)”. Writing “(3.2)” is enough because the numbers of equations are the only references inside curved brackets. Likewise, when citing bibliography, you do not need to write “Bibliography [15]”, because bibliographic reference numbers are the only numbers inside the right brackets.

### About Structure and Content

- Guide the reader through the document. At the end of the introduction provide an outline of the purpose of each chapter. In the beginning of each chapter briefly introduce its contents. For chapters with a lot of content, finalize the chapter with a section that summarizes the main ideas given.
- Logically group your text in paragraphs. A paragraph should be a self-contained group of sentences that, together, try to explain some fact, and that a reader can make sense without reading the other paragraphs.
- Try to identify the meaning of each paragraph in your document. Merge paragraphs that have the same meaning and split paragraphs whose sentences are not interdependent.
- Explain all acronyms the first time you use them.
- Do not use concepts that have not been introduced or defined before in the document.
- In a report it is preferable to include less concepts but written rigorously than many concepts written superficially.

### About Style

- Do not forget to use good grammar and spell checker before sending the document for review. Microsoft Word and Google Docs have good grammar and spell checkers.
- Revise your work many times.
- Read other technical material: scientific papers and magazines are good sources.
- Use short sentences. Consider splitting sentences bigger than 2-3 lines.
- Make sure sentences are well formed: at least a subject followed by a verb, and then an object. Example: “Fires are difficult to detect. Considering there is smoke in the area.” The second sentence is not well formed.
- For the most part, eliminate adverbs and adjectives, which can interfere with the precise, clear, and straightforward writing needed to communicate technical and scientific processes.
- Stay objective. Eliminate opinions, such as “I think” or “I feel”, from your writing so that the emphasis remains on the technical and scientific processes and facts.
- Omit needless words. Unnecessary words distract the reader. Do not write, “This is a system the performance of which is very useful”. Instead, write “This is a useful system”.
- Write in a way that comes naturally. Speak the sentence. If it sounds correct, trust your ear and use the sentence. If it sounds unnatural, rewrite it.
- Avoid fancy words; they do not impress anyone.
- Be clear in your expression. If the idea you are trying to convey is getting lost in a sea of words and phrases, draw a line through the sentence and start again.
- Beware of writing “it’s” instead of “its”, and vice versa. To prevent this error, avoid using informal language abbreviations. Use “do not” instead of “don’t” or “it is” instead of “it’s”.
- Beware of writing “composed by” instead of “composed of”. The 9th symphony is composed by Beethoven. The system is composed of different modules.
- Avoid starting a section with a subsection. Put some text before the subsection.
- Names of sections, figures, tables, chapters, etc. should be written with capitalized initials.
- Always use a comma after the following words, if they start a sentence: “However,”, “Also,”, “Moreover,”, “Thereafter,”, “Furthermore,”, and others.

Recommended reading:

<a href="https://www.griffith.edu.au/__data/assets/pdf_file/0031/825556/Elements-of-Style-1959.pdf" target="_blank" rel="noopener noreferrer">The Elements of Style</a>

## Presentations

### Structure

The presentation of a scientific work must follow a similar structure of a report. Organize your slides according to the chapters in your thesis. If the presentation is short, you may skip some background material.

When changing a chapter, put a separator slide to make clear that you are changing chapter. These separator slides do not count for the overall slide number. It is helpful if you can have a space in your slide that identifies to which chapter it belongs.

### Depth

The depth of the topics to present should be adapted to the available presentation time. Typically, one should consider one slide per minute. Of course, the presenter can be faster than that, but the problem is that the average audience cannot cope with a faster pace.

### Content of the Slides

- Number the slides. The questions may refer to particular slides and it is much easier to do it if slides are numbered.
- Put as many illustrations as possible. Concepts and ideas are much better explained if diagrams and figures are used to accompany the verbal explanations.
- Do not use full sentences: use keywords and/or telegraphic messages. The human brain cannot process written syntax and verbal syntax at the same time. So, if you put a full sentence in the slide, the audience can only read it if it is not listening to your speech, or can only listen to what you are saying if it does not read the slide. So, full sentences are a waste of space and audience attention. Use only keywords in the slides.
- Bibliographic references should be put in the same slide of the citation. It is useless to put the references in a final slide, because the audience cannot recall and associate the references to the slide where they were used.
- Use only one slide to explain one topic and clearly identify the topic in the title of the slide. It is not recommended to break a topic in multiple slides because the audience’s attention is limited and may not keep track of what was explained in the previous slides. Everything about that topic should be in the same slide so people can quickly assess all relevant information.
- Do not overload the slides. Have a large font and figures. Keep the number of important things in a slide to 2-3. Never put animation that occludes the other content of the slide. If you feel the need to do that, it means you need a new slide.

### Presentation

When explaining concepts, put yourself in the role of the audience and ask yourself the question if they can understand what you are saying. You should not speak too fast, and use the least amount of words to explain a concept, possibly using figures to help. Spoken sentences should be short and uncomplicated.

The presentations typically have a period for question and answers, or Q&A, so you do not have to explain everything in the presentation. Leave the more complicated things to the Q&A period, and keep on the presentation only a selection of the topics that give most value to your work.

Spoken discourse is very different from written discourse. So, do not write your speech and read it from paper. People will notice: you will speak too much, your style will be boring, and you will make intonation mistakes that will confuse the audience. Also, do not memorize your speech word by word. This will make you freeze if you forget a word in the sequence, which has a very high probability to happen. Instead, just list the ideas that you want to convey in each slide and use a verbal style to say them. You can put keywords in the slide to remember what are the key ideas that you should tell to the audience.

Make eye contact with the audience, use your hands to help the interaction, point to the elements in the slide you are talking about at each time, and make variations in amplitude and intonation in the aspects that are more important in each slide.

People in the audience, even if they are experts in the topics of your work and read your thesis very carefully, will never be aware of all details about your work. So, it is better to assume that they have not read your work at all, even if they did, and consider that they are trying to understand your work for the first time. They cannot do it if you speak very quickly, or if you go too deep in the explanation, or try to impress them by saying very far-fetched things. Keep things simple.

See other presentations made by experienced people. There is a standard way to do presentations and the audience is expecting a standard format. If you try to innovate too much away from the standard format, it makes things more difficult to understand, no matter how brilliant and creative you may think your presentation is.

As a rule of thumb, you should consider showing one slide per minute. So, if your presentation is 20 min, consider making 20 slides with content. Less than that the audience may find it boring, more than that the audience will not have time to process the information in the slide.

You should have a clear structure for the presentation, divided into sections, that you can present in the initial slides. Then, use slide separators, which do not count for the previous point, identifying when you change sections.

Check more guidelines here:

<a href="https://ethz.ch/content/dam/ethz/special-interest/infk/inst-infsec/information-security-group-dam/education/guide-presentations.pdf" target="_blank" rel="noopener noreferrer">ETH Zurich presentation guidelines</a>