# What is tr-law-rag

A minimal Django-based web application that demonstrates a Legal AI input-to-output flow. This project uses AI semantic search to find relevant legal precedents (emsal kararlar) based on user descriptions.

![WhatsApp Image 2026-01-06 at 23 22 04](https://github.com/user-attachments/assets/0e443ecb-953d-4e76-b96b-550f6b2ae95b)
![WhatsApp Image 2026-01-06 at 23 22 02](https://github.com/user-attachments/assets/6309c440-b37e-4cb0-a8df-0ff317651b09)


# What is RAG and Why is It Important

Retrieval-Augmented Generation (RAG) is an approach that combines large language models with external knowledge sources. Instead of relying solely on the model’s internal training data like LLM's, RAG retrieves relevant documents from a knowledge base and uses them as context when generating responses.

This is especially important in domains like law, where accuracy, traceability, and up-to-date information are critical. By grounding model outputs in real documents, RAG reduces hallucinations, improves factual consistency, and enables more reliable, domain-specific question answering. In tr-law-rag, this approach allows the system to generate answers based on actual Turkish legal decisions rather than general assumptions.

# What Makes tr-law-rag Special?

tr-law-rag is first known RAG model trained on Thousands of Turkish Constitutional Court (Anayasa Mahkemesi) decisions.

## How It Works

This project leverages advanced NLP techniques to provide accurate legal search results:

1.  **Data Processing:** Thousands of Constitutional Court (Anayasa Mahkemesi) decisions were collected and meticulously **cleaned**.
2.  **Embedding:** The processed text was converted into high-dimensional vector embeddings using the **BAAI/bge-m3** model, which is optimized for multi-lingual and long-context understanding.
3.  **Vector Search:** These embeddings are stored in **Qdrant**, a high-performance open-source vector database, enabling millisecond-speed semantic retrieval.

## Installation & Setup

Before running the Django application, you need to set up the Vector Database (Qdrant) with the required data.

### 1. Database Setup (Qdrant)

**Step 1: Download the Data**
First, download the pre-indexed Qdrant data file from Hugging Face:
[https://huggingface.co/datasets/erdem-p/aym-kararlar-qdrant-index](https://huggingface.co/datasets/erdem-p/aym-kararlar-qdrant-index)

**Step 2: Prepare Directory & Run Docker**
Run the following commands to set up the storage directory and start the Qdrant container:

```bash
# Create storage directory
mkdir -p ~/hukuk_ai/qdrant_storage

# Go to the working directory
cd ~/hukuk_ai

# IMPORTANT: Place the downloaded Hugging Face files into the 'qdrant_storage' folder before running Docker.

# Run Qdrant with Docker
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

### 2. Project Setup

**Step 1: Clone the Repository**
Download this repository to your local machine.

```bash
git clone https://github.com/pars-erdem/tr-law-rag.git
cd HukukAi_s
```

**Step 2: Install Dependencies**
Install the required Python packages.

```bash
pip install -r requirements.txt
```
*Alternatively:* `pip install django qdrant-client sentence-transformers python-dotenv`

**Step 3: Configure Environment**
Create a `.env` file in the project root path (`HukukAi_s/.env`) and add your configuration:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Run the Application

Once the database is running and dependencies are installed:

```bash
python manage.py runserver
```

Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

##  Future Plans

The dataset is planned to be expanded and strengthened with decisions from:
- European Court of Human Rights (AIHM)
- Court of Cassation (Yargıtay)
- Council of State (Danıştay)
- Regional Courts of Justice (Bölge Adliye Mahkemeleri)

GGUF quantized model for applications like:
- Local sessions solely for privacy
- Running tr-law-rag on a Raspberry Pi for usecases on the go

##  Disclaimer

This project is a **public demo** and is **not intended for production use**. It is designed solely to demonstrate the functionality of the system.
