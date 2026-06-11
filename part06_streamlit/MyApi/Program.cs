var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.MapGet("/api/hello", () =>
{
    return Results.Ok(new
    {
        Message = "Hello API"
    });
});

app.MapPost("/api/login",
(string id, string password) =>
{
    if (id == "admin" &&
        password == "1234")
    {
        return Results.Ok("로그인 성공");
    }

    return Results.BadRequest("실패");
});

app.Run();