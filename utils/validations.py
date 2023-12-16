
def validate_movie(movie):
    if movie is None:
        return "No movie provided"

    has_title = movie.get('title') is not None
    has_year = movie.get('year') is not None
    has_score = movie.get('score') is not None

    message = "The missing fields are: "

    if not has_title:
        message += 'title'
    if not has_year:
        message += ", " + 'year' if not has_title else 'year'
    if not has_score:
        message += ", " + 'score' if not has_year else 'score'

    if not has_year and not has_score and not has_title:
        message = "The missing fields are: title, year and score"

    return message
