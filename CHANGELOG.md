# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

   - JWT authentication flow
   - The front-end

## [0.0.4] - 2022-04-15
### Changed
   - Reset password message translated to english

### Added
   - .xlsx files generation with the words registered byt the user
   - CRUD of words

## [0.0.3] - 2022-04-09
### Changed
   - Moved .gitignore to root folder
   - Small changes on README.md

### Added
   - Words CRUD (schemas, crud functions and routes)

## [0.0.2] - 2022-03-20
### Changed
   - Moved all exceptions to exceptions.py file
   - Created relationship on models/users.py with models/words.py because of foreign key

### Added
   - Words table
   - Argument 'echo' at the create_engine function in database.py to keep track of the database queries on the server log

## [0.0.1] - 2021-10-30
### Added
   - CRUD of users, as well as a very simple authentication flow 
