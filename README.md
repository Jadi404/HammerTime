# Hammer Time Auctioneering Platform (WIP)

A full-stack web application that simulates an auctioneering platform for cars, properties, and farming equipment.

This project is being built to showcase full-stack development skills, including API design, database architecture, and modern frontend integration.


## Status

🚧 Work in Progress

Current progress:

* ✅ Wireframes designed (Figma)
* ✅ Backend API setup (FastAPI)
* ✅ Database models created


## Features (Planned & In Progress)

*  View all auction listings
*  Filter by category (Cars, Houses, Farming Equipment)
*  Auction detail page
*  Live bidding system (top 10 bids displayed)
*  Bidder count per auction
*  Auction countdown timer *(planned)*
*  User authentication *(planned)*

## Tech Stack

### Frontend

* React (Vite)
* JavaScript
* CSS (custom styling)

### Backend

* FastAPI (Python)
* SQLAlchemy
* SQLite (development)

### Tools

* Git & GitHub
* Figma (UI/UX design)


## 🗂 Project Structure

```
HammerTime/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── routes/
│   │   │   ├── auctions.py
│   │   │   └── bids.py
│
├── frontend/
│   ├── src/
│   ├── index.html
│
└── README.md
```

---

## Running the Project Locally

### 1. Clone the repo - NOT RECOMMENED (WIP)

```
To Be Announced
```

---

### 2. Backend Setup

```
To Be Announced
```
---

### 3. Frontend Setup

```
To Be Announced
```


## API Endpoints

### Auctions

* `GET /auctions` → Get all auctions
* `GET /auctions/{id}` → Get auction details

### Bids

* `GET /auctions/{id}/bids` → Top 10 bids
* `POST /auctions/{id}/bid` → Place a bid


## Learning Goals

* Build a structured backend using FastAPI
* Design and interact with relational databases
* Connect a frontend UI to a REST API
* Practice clean architecture and scalable project structure


## Screenshots

*(Coming soon)*


## Future Improvements

* To Be Established
  


## 👤 Author

Jade Carreira
Aspiring Full Stack Developer | Technical Artist

---

## Notes

This is a portfolio project under active development. Features and structure may evolve as the project grows. Any likeness or referencing is purely co-incidental and this is not a live auctioneering site. 
