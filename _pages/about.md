---
permalink: /
layout: single
author_profile: false
classes: wide
title: ""
redirect_from:
  - /about/
  - /about.html
---

<div class="research-home">
  <section class="hero" id="home" aria-labelledby="hero-title">
    <div class="hero-portrait"><img src="{{ '/images/profile-photo.jpg' | relative_url }}" alt="Portrait of Hongyu Xia"></div>
    <div class="hero-copy">
      <h1 id="hero-title">Hongyu Xia</h1>
      <p class="hero-department">School of Computer Science and Technology</p>
      <p class="hero-affiliation">Harbin Institute of Technology (Shenzhen)</p>
      <p class="hero-role">Ph.D. Student in Computer Science and Technology</p>
      <p class="hero-summary">I am advised by <a class="advisor-link" href="https://wenjiepei.github.io/" target="_blank" rel="noopener"><strong>Prof. Wenjie Pei</strong></a> and work on generative AI for controllable visual creation, world modeling, and computer vision.</p>
    </div>
    <aside class="hero-aside" aria-label="Research interests and contact links">
      <h2>Research Interests</h2>
      <ul class="interest-list">
        <li>Generative AI</li>
        <li>Controllable Image &amp; Video Editing</li>
        <li>World Models</li>
        <li>Computer Vision</li>
      </ul>
      <div class="profile-links">
        <a href="mailto:26b951110@stu.hit.edu.cn"><span aria-hidden="true">@</span>Email</a>
        <a href="https://github.com/XHYuu" target="_blank" rel="noopener"><span aria-hidden="true">GH</span>GitHub</a>
      </div>
    </aside>
  </section>

  <section class="home-section about-detail" id="about">
    <div class="about-heading"><p class="section-kicker">About</p><h2>About me</h2></div>
    <div class="about-copy">
      <div class="about-language">
        <p>I am a Ph.D. student in Computer Science and Technology at Harbin Institute of Technology (Shenzhen), advised by <a class="advisor-link" href="https://wenjiepei.github.io/" target="_blank" rel="noopener"><strong>Prof. Wenjie Pei</strong></a>. My research focuses on generative AI, controllable image and video editing, world models, and computer vision.</p>
        <p>I aim to build controllable and generalizable generative systems that connect visual creation, perception, and interaction. Before joining HIT (Shenzhen), I completed an M.Sc. in Artificial Intelligence at The University of Hong Kong and a B.E. in Computer Science and Technology at Central South University.</p>
      </div>
      <div class="about-language about-zh" lang="zh-CN">
        <p>我目前在哈尔滨工业大学（深圳）计算机科学与技术学院攻读计算机科学与技术博士学位，导师为<a class="advisor-link" href="https://wenjiepei.github.io/" target="_blank" rel="noopener"><strong>裴文杰教授</strong></a>。我的研究方向包括生成式人工智能、可控图像与视频编辑、世界模型和计算机视觉。</p>
        <p>我的研究目标是构建可控、具备良好泛化能力的生成式系统，连接视觉内容生成、感知与交互。在进入哈尔滨工业大学（深圳）之前，我于香港大学获得人工智能理学硕士学位，并于中南大学获得计算机科学与技术工学学士学位。</p>
      </div>
    </div>
  </section>

  <section class="research-plan" id="research-plan">
    <div class="plan-meta"><p class="section-kicker">Latest research plan</p><p>Updated {{ site.data.research_plan.updated }}</p></div>
    <div class="plan-content">
      <h2>{{ site.data.research_plan.title }}</h2>
      <p class="plan-lead">{{ site.data.research_plan.summary }}</p>
      <p>{{ site.data.research_plan.detail }}</p>
      <div class="plan-tags">{% for tag in site.data.research_plan.tags %}<span>{{ tag }}</span>{% endfor %}</div>
      <p class="plan-invitation">{{ site.data.research_plan.invitation }}</p>
    </div>
  </section>

  <section class="home-section" id="research">
    <div class="section-heading" id="publications"><div><p class="section-kicker">Research</p><h2>Selected publications</h2></div></div>
    <div class="work-list">
      <article class="work-row has-media">
        <div class="work-thumbnail"><img src="{{ '/images/DRDD-poster.jpg' | relative_url }}" alt="Poster for Decoupled Residual Denoising Diffusion Models" loading="lazy"></div>
        <div class="work-copy"><p class="work-venue"><em>Computer Vision and Pattern Recognition</em> Conference · CVPR 2026</p><h3>Decoupled Residual Denoising Diffusion Models for Unified and Data-Efficient Image-to-Image Translation</h3><p class="work-authors">Ziyue Lin*, Jiahe Hou*, <strong>Hongyu Xia*</strong>, Xinrui Xie, Feifei Wang, Yuyin Zhou, Wei Wang, Jiawei Liu, and Liangqiong Qu</p><p>Decouples diffusion into stochastic domain alignment and deterministic semantic mapping for unified, data-efficient image-to-image translation.</p><div class="work-links"><a href="https://arxiv.org/abs/2606.01048" target="_blank" rel="noopener">Paper</a><a href="https://github.com/HKU-HealthAI/DRDD" target="_blank" rel="noopener">Project</a></div></div>
      </article>
      <article class="work-row no-media">
        <div class="work-copy"><p class="work-venue">China Automation Congress (CAC) · 2023</p><h3>A Method of Vehicle Peripheral Objects Detection Based on Binocular Vision</h3><p class="work-authors">Xinyu Wang, <strong>Hongyu Xia</strong>, Zhichen Huang, Zihao Yuan, and Wei Zhou</p><p>A binocular-vision approach for detecting objects around vehicles and supporting robust environmental perception.</p><div class="work-links"><a href="https://ieeexplore.ieee.org/abstract/document/10451039/" target="_blank" rel="noopener">Paper</a></div></div>
      </article>
    </div>

    <div class="subsection-heading"><p class="section-kicker">Projects</p><h2>Selected projects</h2></div>
    <div class="work-list project-list">
      <article class="work-row no-media"><div class="work-copy"><p class="work-venue">Central South University · 2023–2024</p><h3>Diseased Cell Detection with Vision-Language Models</h3><p>Developed a multimodal method combining cell imagery and textual information for detection and classification while reducing reliance on large annotated datasets.</p></div></article>
      <article class="work-row no-media"><div class="work-copy"><p class="work-venue">Central South University · 2022–2023</p><h3>Rotation-Invariant Object Detection</h3><p>Designed a CNN–Transformer architecture for rotation-robust target detection and evaluated its generalization across object categories and orientations.</p></div></article>
    </div>
  </section>

  <section class="home-section" id="education">
    <div class="section-heading"><div><p class="section-kicker">Education</p><h2>Academic journey</h2></div></div>
    <div class="timeline"><article><span class="timeline-dot"></span><p class="meta">2025–Present</p><h3>Harbin Institute of Technology (Shenzhen)</h3><p>Ph.D. in Computer Science and Technology<br>Advisor: <a class="advisor-link" href="https://wenjiepei.github.io/" target="_blank" rel="noopener">Prof. Wenjie Pei</a></p></article><article><span class="timeline-dot"></span><p class="meta">2024–2025</p><h3>The University of Hong Kong</h3><p>M.Sc. in Artificial Intelligence</p></article><article><span class="timeline-dot"></span><p class="meta">2020–2024</p><h3>Central South University</h3><p>B.E. in Computer Science and Technology</p></article></div>
  </section>

  <section class="home-section" id="awards">
    <div class="section-heading"><div><p class="section-kicker">Recognition</p><h2>Honors &amp; awards</h2></div><p>Selected recognition for academic achievement, innovation, and student research.</p></div>
    <div class="awards-grid">
      <article class="award-card"><span class="award-mark" aria-hidden="true">01</span><div><p class="award-type">Academic distinction</p><h3>Individual Scholarship</h3><p>Central South University</p></div></article>
      <article class="award-card"><span class="award-mark" aria-hidden="true">02</span><div><p class="award-type">Innovation</p><h3>Innovation &amp; Entrepreneurship Competition Awards</h3><p>Recognition for student-led technology and innovation projects</p></div></article>
      <article class="award-card"><span class="award-mark" aria-hidden="true">03</span><div><p class="award-type">Student research</p><h3>Outstanding Student Innovation Project</h3><p>Recognition for undergraduate research and project development</p></div></article>
    </div>
  </section>

  <section class="home-section contact-panel" id="contact"><p class="section-kicker">Contact</p><h2>Interested in generative visual intelligence?</h2><p>I welcome conversations about research, collaboration, and new ideas in generative AI.</p><a class="button button-light" href="mailto:26b951110@stu.hit.edu.cn">Get in touch</a></section>
</div>

