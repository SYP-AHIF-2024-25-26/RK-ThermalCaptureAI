var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
// builder.Services.AddEndpointsApiExplorer();
// builder.Services.AddSwaggerGen();

var app = builder.Build();

// // Configure the HTTP request pipeline.
// if (app.Environment.IsDevelopment()) {
//     app.UseSwagger();
//     app.UseSwaggerUI();
// }

app.UseHttpsRedirection();

app.MapGet("/", (HttpResponse response) => Results.Ok("online"));

app.MapPost("/upload", async (HttpRequest request) => {
    if (!request.HasFormContentType) {
        return Results.BadRequest("Invalid form content type");
    }

    var form = await request.ReadFormAsync();
    var file = form.Files.FirstOrDefault();

    if (file == null || file.Length == 0) {
        return Results.BadRequest("No file uploaded");
    }

    Console.WriteLine(file.Name);
    var filePath = Path.Combine("uploads", file.FileName);

    using (var stream = new FileStream(filePath, FileMode.Create)) {
        await file.CopyToAsync(stream);
    }

    return Results.Ok("File uploaded successfully");
});

app.Run();