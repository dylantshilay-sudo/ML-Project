# Fintech Wallet API

A backend fintech wallet application built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. This project was developed to strengthen my backend engineering skills by designing a modular REST API that simulates core features of a digital wallet.

The application follows a layered architecture, separating routing, business logic, database models, and schemas to improve maintainability and scalability.

---

## Features

- User registration and authentication
- Secure login with JWT authentication
- Wallet creation and management
- Balance management
- Transaction history
- Virtual card creation
- Payment provider integration
- Webhook handling
- PostgreSQL database
- Interactive API documentation

---

## Project Structure

```
Backend Wallet/
│
├── auth/           # Authentication & security
├── models/         # SQLAlchemy database models
├── router/         # API endpoints
├── schemas/        # Pydantic schemas
├── services/       # Business logic
├── database.py     # Database configuration
├── config.py       # Application settings
└── main.py         # FastAPI application
```

---

## Technologies

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT Authentication
- RESTful APIs
- Git & GitHub

---

## Database

The application uses **PostgreSQL** as its relational database and **SQLAlchemy ORM** for database interactions.

The data model includes relationships between:

- Users
- Wallets
- Transactions
- Cards

This project helped me gain practical experience with relational database design, SQL, foreign keys, ORM relationships, and CRUD operations.

---

## What I Learned

Building this project allowed me to improve my understanding of:

- Backend application architecture
- REST API development
- Authentication and authorization
- SQLAlchemy ORM
- PostgreSQL database design
- Business logic separation
- Error handling
- API documentation
- Project organization

---

## API Documentation

Interactive Swagger documentation is available here:

**https://web-production-c411b0.up.railway.app/docs**

---

## Live Demo

The project is deployed on Railway:

**https://fintechwallet.up.railway.app/**

---

## Purpose

This project is part of my backend engineering portfolio.

My goal was not only to build a working API but also to practice writing clean, organized, and scalable backend code while applying modern backend development principles.

As I continue learning Java and Spring Boot, I plan to build similar backend applications using the same engineering concepts.

---

Thank you for visiting this repository!
