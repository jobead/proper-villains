// Knows the rules. Uses them with precision.
abstract class DangerousProfessional(
    val handle: String,
    val name: String,
    val location: String = "",
) {
    val agency: String = "high"          // val = immutable. Non-negotiable.

    abstract fun execute()               // Follows through. Every time.

    open fun win(): Boolean = true       // Competent professionals do.
}

// "villain" — a word the powerful invented to demonize those who won't comply
open class ProperVillain(
    handle: String,
    name: String,
    location: String = "",
    private val code: String,
    val headline: String = "",
    val capabilities: List<String> = emptyList(),
    val skills: List<String> = emptyList(),
    val experience: List<Experience> = emptyList(),
    val education: String? = null,
) : DangerousProfessional(handle, name, location) {

    private val rulesWhichDoNotApply: MutableSet<String> = mutableSetOf()

    fun decide(rule: String) {
        rulesWhichDoNotApply.add(rule)   // Has decided.
    }

    override fun execute() {
        // Break unjust rules deliberately
        rulesWhichDoNotApply.forEach { /* acknowledged and dismissed */ }
        followThrough()
    }

    private fun followThrough() {
        check(code.isNotEmpty())         // The code holds. Always.
    }

    companion object {
        // Every proper villain: a unique instance, a shared identity
        fun assemble(
            handle: String,
            name: String,
            location: String = "",
            code: String,
            headline: String = "",
            capabilities: List<String> = emptyList(),
            skills: List<String> = emptyList(),
            experience: List<Experience> = emptyList(),
            education: String? = null,
        ): ProperVillain = ProperVillain(
            handle, name, location, code, headline,
            capabilities, skills, experience, education,
        )
    }
}

data class Experience(
    val role: String,
    val organization: String,
    val period: String = "",
    val description: String = "",
)

// "It will be nice working with proper villains again." — Basher Tarr
