# Secure Shop API

A realistic e-commerce backend built for testing repository intelligence platforms.

## Architecture Overview
This project uses a layered architecture to cleanly separate concerns.
- **app/api/**: API endpoints and route handlers.
- **app/services/**: Core business logic.
- **app/repositories/**: Data access layer.
- **app/models/**: Domain entities.
- **app/security/**: Authentication and authorization logic.
- **app/utils/**: Helper functions.
- **app/database/**: Database connection management.
- **app/config/**: Application settings.

## Service Relationships and Request Flow
Example flow for placing an order:
1. `POST /api/orders` hits `app/api/orders.py`
2. `orders.py` calls `OrderService.place_order()`
3. `OrderService` uses `OrderRepository` to save the order
4. `OrderService` calls `PaymentService.charge()`
5. `PaymentService` calls `NotificationService.send_receipt()`
6. `NotificationService` uses `EmailSender.send()`