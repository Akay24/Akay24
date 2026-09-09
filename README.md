<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=190&section=header&text=Abhijeet%20Mishra&fontSize=42&fontColor=ffffff&animation=twinkling&fontAlignY=36&desc=Backend%20SDE%20%7C%20Agentic%20AI%20Systems%20%7C%20Distributed%20Infrastructure&descSize=15&descColor=c9d1d9&descAlignY=62" alt="Header" width="100%"/>

<a href="https://readme-typing-svg.demolab.com">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=16&pause=1200&color=58A6FF&center=true&vCenter=true&width=650&lines=Backend+Software+Development+Engineer;Agentic+AI+Pipelines+(LangGraph+%2B+Amazon+Bedrock);Author+of+reportkit-py+(Published+on+PyPI);Building+CodeSentinel+(Autonomous+Coding+Agent);Distributed+Systems+%C2%B7+High-Throughput+APIs" alt="Typing SVG" />
</a>

<br/>

[![PyPI](https://img.shields.io/pypi/v/reportkit-py?label=PyPI%3A%20reportkit-py&color=3776AB&style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/reportkit-py/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhijeet-mishra-76bb7a204/)
[![Email](https://img.shields.io/badge/Email-abhijeetmishra2410%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:abhijeetmishra2410@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Akay24-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Akay24)

</div>

<br/>

<div align="justify">

Backend Software Engineer specializing in **agentic AI systems** and **production backend infrastructure**. My work centers on architecting multi-agent automation pipelines (LangGraph, Amazon Bedrock, Pinecone RAG), shipping high-uptime microservices in Python and Node.js on AWS, and engineering developer tooling. I am the author of [**reportkit-py**](https://pypi.org/project/reportkit-py/), an open-source OOXML document rendering engine published on PyPI.

</div>

<br/>

## ◈ Active Engineering Pipeline

<table>
<thead>
<tr>
<th align="left">Status</th>
<th align="left">Project / Initiative</th>
<th align="left">Core Architecture & Focus</th>
<th align="right">Target / Link</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://img.shields.io/badge/In%20Progress-FFA500?style=flat-square" alt="In Progress"/></td>
<td><b>CodeSentinel</b></td>
<td>Autonomous coding agent: generates RAG-grounded diffs with LangGraph & Claude on Bedrock, verified in isolated test sandboxes</td>
<td align="right"><code>Agentic AI</code></td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/PyPI%20Live-brightgreen?style=flat-square" alt="PyPI Live"/></td>
<td><b><a href="https://github.com/Akay24/reportkit-py">reportkit-py</a></b></td>
<td>Lightweight Python library: parses HTML/Nunjucks into DOCX with native editable Office charts and DOCX-to-PDF pipeline</td>
<td align="right"><a href="https://pypi.org/project/reportkit-py/"><code>pip install</code> ↗</a></td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Production-007ACC?style=flat-square" alt="Production"/></td>
<td><b>Enterprise Agentic Pipeline</b></td>
<td>Multi-agent automation system: Pinecone vector search, automated Playwright screenshot triage, automated report generation</td>
<td align="right"><code>Enterprise System</code></td>
</tr>
<tr>
<td><img src="https://img.shields.io/badge/Interactive-9cf?style=flat-square" alt="Interactive"/></td>
<td><b><a href="https://github.com/Akay24/Chess-Engine">TwentyFish</a></b></td>
<td>Chess platform featuring 20 Stockfish-calibrated difficulty tiers (~200 Elo steps) via WASM in dedicated Web Workers</td>
<td align="right"><a href="https://github.com/Akay24/Chess-Engine"><code>Source</code> ↗</a></td>
</tr>
</tbody>
</table>

<br/>

## ◈ Featured Architecture Showcases

<table>
<tr>
<td width="50%" valign="top">

### 🤖 [CodeSentinel](https://github.com/Akay24)
<sub>Autonomous Coding & Verification Agent</sub>

<div align="justify">

An agentic automation system engineered to resolve GitHub issues with strict safety boundaries. Ingests issue descriptions, retrieves codebase context via vector search, generates patches using <b>LangGraph + Claude on Amazon Bedrock</b>, and executes an automated generate-verify-repair loop inside an isolated Docker sandbox.

</div>

* **Deterministic Verification Loop:** Iterates on unit test and lint failures inside the container before generating a PR.
* **Safety By Design:** Strict human-in-the-loop requirement — never auto-merges patches into branches.
* **Execution Telemetry:** Emits structured step-by-step diagnostic reports with execution logs and coverage diffs.

<br/>

![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=flat-square&logo=diagram-project&logoColor=white)
![Amazon Bedrock](https://img.shields.io/badge/Amazon_Bedrock-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![Claude 3.5](https://img.shields.io/badge/Claude-D97706?style=flat-square&logo=anthropic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker_Sandbox-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### 📦 [reportkit-py](https://github.com/Akay24/reportkit-py)
<sub>HTML/Nunjucks → DOCX/PDF Engine (PyPI Published)</sub>

<div align="justify">

Production Python package built to eliminate costly third-party rendering APIs and bloated headless browsers. Converts HTML/Nunjucks templates directly into Microsoft Word documents with <b>native, editable Office XML charts</b> (not rasterized images), paired with automated DOCX-to-PDF conversion.

</div>

* **Native OpenXML Pipeline:** Directly manipulates the underlying WordProcessingML package for lightweight execution.
* **Footprint Optimization:** Slashes memory footprint from ~800MB (headless Chromium) to <80MB per worker process.
* **Dual Deployment Model:** Consumable as a lightweight library or deployed as a containerized Flask REST microservice.

<br/>

[![PyPI](https://img.shields.io/pypi/v/reportkit-py?color=3776AB&style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/reportkit-py/)
![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![OOXML](https://img.shields.io/badge/OOXML-Custom_Pipeline-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ♟️ [TwentyFish](https://github.com/Akay24/Chess-Engine)
<sub>Calibrated Chess Engine & Analysis Platform</sub>

<div align="justify">

A full-stack chess platform featuring <b>20 granular difficulty levels</b>, each calibrated to ~200 Elo intervals using UCI parameter tuning (Skill Level, Depth, Error Rate, and time handicaps) powered by Stockfish compiled to WebAssembly.

</div>

* **Non-Blocking Worker Architecture:** Offloads Stockfish WASM minimax tree search to dedicated Web Workers, preserving a smooth 60fps UI thread.
* **Full Analysis Suite:** Live dynamic evaluation bar, interactive move tree exploration, PGN export, and opening book integration.
* **Automated Test Suite:** Comprehensive end-to-end test suite built with Playwright covering engine state and move legality.

<br/>

![Next.js](https://img.shields.io/badge/Next.js_14-000?style=flat-square&logo=nextdotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![WASM](https://img.shields.io/badge/Stockfish-WASM-654FF0?style=flat-square&logo=webassembly&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-E2E-2EAD33?style=flat-square&logo=playwright&logoColor=white)

</td>
<td width="50%" valign="top">

### 🌐 [SCVRI](https://github.com/Akay24/SCVRI)
<sub>Supply Chain Visibility & Risk Intelligence</sub>

<div align="justify">

Enterprise platform aggregating global supplier networks, shipment tracking events, and external disruption feeds into an actionable triage command center. Employs ML risk models to predict supply chain bottlenecks before disruptions propagate.

</div>

* **Decoupled Microservice Topology:** FastAPI backend isolates high-frequency external feed ingestion from customer-facing query endpoints.
* **Dual-Tier Data Layer:** PostgreSQL for relational supplier graphs paired with Redis for low-latency session and alert caching.
* **Geospatial Command Center:** Next.js reactive frontend with interactive geospatial mapping and multi-tier alert triage workflows.

<br/>

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000?style=flat-square&logo=nextdotjs&logoColor=white)

</td>
</tr>
</table>

<br/>

## ◈ Engineering Principles & System Design

<div align="justify">

* **Deterministic Verification Over Generative Guesswork:** Large language models propose modifications; isolated compilers, test runners, and linters deterministically verify them in ephemeral environments before human review.
* **Lean Runtime Footprints:** Avoid heavy runtime dependencies (e.g. headless browsers) where native protocols or direct binary formats (e.g. OpenXML) accomplish the objective with 10x lower memory overhead.
* **Decoupled Compute Topologies:** Keep long-running or CPU-intensive workloads (WASM minimax engines, batch document rendering, vector search) off critical request and UI threads via asynchronous workers and background queues.
* **Defensive API Boundaries:** Enforce strict contract validation, structured audit trails, and least-privilege access patterns across all microservice boundaries.

</div>

<br/>

## ◈ Technical Arsenal

<div align="center">

### AI, Agents & Vector Intelligence
<img src="https://img.shields.io/badge/LangGraph-000000?style=for-the-badge&logo=diagram-project&logoColor=white" alt="LangGraph"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"/>
<img src="https://img.shields.io/badge/Amazon_Bedrock-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" alt="Amazon Bedrock"/>
<img src="https://img.shields.io/badge/Claude-D97706?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude"/>
<img src="https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logo=pinecone&logoColor=white" alt="Pinecone"/>
<img src="https://img.shields.io/badge/RAG_Pipelines-4B32C3?style=for-the-badge&logo=databricks&logoColor=white" alt="RAG"/>

<br/><br/>

### Core Languages & Ecosystem
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=python,js,ts,cpp,c&theme=dark" alt="Languages" />
</a>

<br/>

### Backend Frameworks, APIs & Data Stores
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=fastapi,nodejs,express,flask,postgres,mongodb,redis,mysql&theme=dark" alt="Backend & Databases" />
</a>

<br/>

### Cloud Infrastructure, Testing & DevOps
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=aws,docker,jenkins,git,github,postman&theme=dark" alt="Cloud & DevOps" />
</a>

<br/>

</div>

<br/>

## ◈ System Telemetry & GitHub Analytics

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=akay24&theme=github_dark" alt="Contribution Graph" width="100%"/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=akay24&theme=tokyonight&hide_border=true" alt="Contribution Streak" width="49%"/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=akay24&theme=github_dark&utcOffset=5.5" alt="Productive Time" width="49%"/>

<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=akay24&theme=github_dark" alt="Top Languages" width="49%"/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=akay24&theme=github_dark" alt="GitHub Stats" width="49%"/>

</div>

<br/>

---

<div align="center">

*"Reliability is not an accident of good intentions; it is the deliberate output of verifiable feedback loops."*

<br/><br/>

**Abhijeet Mishra** · Software Development Engineer · Bhubaneswar, India 🇮🇳<br/>
<sub>Engineering agentic pipelines, distributed systems, and verifiable software.</sub>

</div>
