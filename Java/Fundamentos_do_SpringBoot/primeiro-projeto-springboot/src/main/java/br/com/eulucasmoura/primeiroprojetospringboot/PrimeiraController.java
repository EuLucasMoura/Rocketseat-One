package br.com.eulucasmoura.primeiroprojetospringboot;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/primeiraController")

public class PrimeiraController {
    
    @GetMapping("/primeiroMetodo")
    public String primeiroMetodo() {
        return "Parabens você criou sua primeira rota!";
    }
}
