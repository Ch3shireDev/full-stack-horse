using System.Linq;
using api.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace api.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ApiController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public ApiController(ILogger<ApiController> logger, ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet("test")]
        public ActionResult Test()
        {
            return Ok("test");
        }

        [HttpGet("messages")]
        public ActionResult Get()
        {
            return Ok(_context.Messages.ToList());
        }

        [HttpPost("messages")]
        public ActionResult Post(Message message)
        {
            _context.Messages.Add(message);
            _context.SaveChanges();
            return Ok(message);
        }
    }
}