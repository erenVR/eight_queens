CREATE TABLE board
  (
     id         BIGSERIAL NOT NULL CONSTRAINT board_pkey PRIMARY KEY,
     size       INTEGER NOT NULL,
     dt_created TIMESTAMP NOT NULL
  );

CREATE UNIQUE INDEX board_board_id_uindex
  ON board (id);

CREATE TABLE queen_position
  (
     id       BIGSERIAL NOT NULL CONSTRAINT queen_position_pkey PRIMARY KEY,
     row      INTEGER DEFAULT 0 NOT NULL,
     col      INTEGER DEFAULT 0 NOT NULL,
     board_id BIGINT NOT NULL
  );

CREATE UNIQUE INDEX queen_position_queen_position_id_uindex
  ON queen_position (id);