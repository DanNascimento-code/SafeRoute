SafeRoute is a safety-focused navigation application designed to help users—especially women—choose safer routes in urban environments. Instead of optimizing only for distance or time, the system evaluates multiple real-world risk factors such as lighting conditions, historical crime data, and environmental context to generate routes that prioritize personal safety.

The application integrates mapping services with external data sources and applies a custom risk-scoring model to analyze and compare possible paths. Users can visualize safer alternatives, understand why a route is considered safer, and make informed decisions in real time.

The project is built with a full-stack architecture using Django on the backend and a modern frontend (React), focusing on scalability, real-world data integration, and practical usability. 


# SafeRoute

SafeRoute is a safety-first navigation application that helps users find safer routes in urban areas by analyzing environmental and contextual risk factors.

## Overview

Traditional navigation systems optimize for speed and distance. SafeRoute introduces a different approach: route optimization based on safety.

The application evaluates multiple variables such as:

* Historical crime data
* Street lighting conditions
* Time of day
* Environmental context

Using these inputs, SafeRoute calculates a **risk score** for different routes and suggests safer alternatives to the user.

## Features

* Safety-based route recommendations
* Risk score calculation for each route
* Integration with real-world data sources
* Interactive map visualization
* Scalable backend architecture

## Tech Stack

**Backend**

* Django
* Django REST Framework

**Frontend**

* React

**APIs & Services**

* Mapbox (or similar mapping service)
* External datasets (crime data, environmental data)

## Architecture

The project follows a modular and scalable architecture:

* Core backend services for route analysis and risk scoring
* API layer for communication between frontend and backend
* Frontend interface for user interaction and visualization

## Goals

* Provide safer navigation alternatives for users
* Demonstrate real-world backend engineering skills
* Work with external APIs and dynamic data sources
* Build a scalable and production-ready system

## Status

Work in progress — currently focusing on:

* Data integration
* Risk modeling
* Route analysis logic

## Future Improvements

* Machine learning-based risk prediction
* Real-time data updates
* User personalization
* Mobile-friendly interface